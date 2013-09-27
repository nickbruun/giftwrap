from .base import Rule


class LogDirectoryRule(Rule):
    """Log directory rule.
    
    :ivar name: Log directory name.
    :ivar user: default `root`, Username to execute an application as.
    :ivar group: default ``None``, Group name to execute an application under.
    """
    
    def __init__(self, name, user = 'root', group = None):
        """Initialize a log directory rule.
        
        :param name: Log directory name.
        :param user: default `root`, Username to execute an application as.
        :ivar group:
            default ``None``, Group name to execute an application under.
        """

        self._name = name
        self._user = user
        self._group = group

    def apply(self, package, context):
        # Create the log directory.
        log_path = '/var/log/%s' % (self._name)
        context.make_data_dir(log_path, 
                              user = self._user, 
                              group = self._group)
