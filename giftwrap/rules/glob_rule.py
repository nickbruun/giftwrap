import os
import fnmatch
import shutil
import stat
from .base import Rule


class GlobRule(Rule):
    """Glob rule.

    Copies a glob into the target.

    :ivar user: default `root`, Username to execute an application as.
    :ivar group: default ``None``, Group name to execute an application under.
    """

    def __init__(self,
                 source_dir,
                 destination_dir,
                 ignore=[],
                 user=None,
                 group=None):
        """Initialize a glob rule.

        :param source_dir: Source directory path.
        :param destination_dir: Destination directory path.
        :param ignore: Files and patterns to ignore.
        :param user: default `root`, Username.
        :param group: default ``None``, Group name.
        """

        self.source_dir = source_dir
        self.destination_dir = destination_dir
        self.ignore = ignore
        self.user = user
        self.group = group

    def apply(self, package, context):
        # Copy!
        destination_dir = context.data_dir_path(self.destination_dir)

        def synchronize_path(rel_dir):
            abs_source_dir = os.path.join(self.source_dir,
                                          rel_dir)
            abs_destination_dir = os.path.join(destination_dir,
                                               rel_dir)

            if not os.path.exists(abs_destination_dir):
                os.mkdir(abs_destination_dir)
                os.chmod(abs_destination_dir,
                         0755)

            for rel_path in os.listdir(abs_source_dir):
                do_skip = False
                for ignore_pattern in self.ignore:
                    if fnmatch.fnmatch(rel_path,
                                       ignore_pattern):
                        do_skip = True
                        break
                if do_skip:
                    continue

                abs_source_path = os.path.join(abs_source_dir,
                                               rel_path)
                abs_destination_path = os.path.join(abs_destination_dir,
                                                    rel_path)

                if os.path.isdir(abs_source_path):
                    synchronize_path(os.path.join(rel_dir,
                                                  rel_path))
                else:
                    shutil.copyfile(abs_source_path,
                                    abs_destination_path)
                    os.chmod(abs_destination_path,
                             0755 if (
                                stat.S_IXUSR &
                                os.stat(abs_source_path)[stat.ST_MODE])
                             else 0644)

        synchronize_path('')
