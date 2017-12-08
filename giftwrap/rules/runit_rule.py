from ..utilities import stringify_args, write_lines_to_file
from .base import Rule


class RunItRule(Rule):
    """runit rule.

    :ivar name:
        Identifier name. Used for both the service and the logging directory.
    :ivar args:
        Application execution arguments like for subprocess invocations.
    :ivar user: default `root`, Username to execute an application as.
    :ivar group: default ``None``, Group name to execute an application under.
    :ivar cwd: default ``None``, Working directory for the application.
    """

    def __init__(self, name, args, user='root', group=None, cwd=None):
        """Initialize a runit rule.

        :param name:
            Identifier name. Used for both the service and the logging
            directory.
        :param args:
            Application execution arguments. If a :class:`str` instance is
            supplied, it is split if it contains whitespaces, or simply created
            as the command.
        :param user: default `root`, Username to execute an application as.
        :ivar group:
            default ``None``, Group name to execute an application under.
        :param cwd: default ``None``, Working directory for the application.
        """

        if isinstance(args, str):
            self._args = args.split(' ')
        elif isinstance(args, list):
            self._args = args
        elif isinstance(args, tuple):
            self._args = list(args)
        else:
            raise TypeError('invalid argument list for args')

        self._name = name
        self._user = user
        self._group = group
        self._cwd = cwd

    def apply(self, package, context):
        package.add_dependency('runit')

        # Create the log directory.
        log_path = '/var/log/%s' % (self._name)
        context.make_data_dir(log_path,
                              user=self._user,
                              group=self._group)

        # Build the run script.
        run_lines = ['#!/bin/sh']

        if self._user is not None:
            run_lines += ['umask 002']

        if self._cwd is not None:
            run_lines += ['cd %s' % (self._cwd)]

        run_lines += ['exec 2>&1']

        if self._user is not None:
            run_lines += ['exec chpst -u%s %s' % (self._user,
                                                  stringify_args(self._args))]
        else:
            run_lines += ['exec chpst %s' % (stringify_args(self._args))]

        # Build the log run script.
        log_run_lines = ['#!/bin/sh']

        if self._user is not None:
            log_run_lines += ['exec chpst -u%s svlogd -tt %s' % (self._user,
                                                                 log_path)]
        else:
            log_run_lines += ['exec svlogd -tt %s' % (log_path)]

        # Write the scripts to their location.
        write_lines_to_file(run_lines,
                            context.data_path('/etc/service/%s/run' %
                                              (self._name)),
                            permissions=0o755)
        write_lines_to_file(log_run_lines,
                            context.data_path('/etc/service/%s/log/run' %
                                              (self._name)),
                            permissions=0o755)
