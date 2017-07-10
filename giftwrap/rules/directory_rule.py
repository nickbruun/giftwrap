from .base import Rule


class DirectoryRule(Rule):
    """Directory rule.

    :ivar path: Directory path.
    :ivar user: default `root`, Username to execute an application as.
    :ivar group: default ``None``, Group name to execute an application under.
    """

    def __init__(self, path, user=None, group=None):
        """Initialize a directory rule.

        :param path: Directory path.
        :param user: default `root`, Username.
        :param group: default ``None``, Group name.
        """

        self.path = path
        self.user = user
        self.group = group

    def apply(self, package, context):
        context.data_dir_path(self.path,
                              user=self.user,
                              group=self.group)
