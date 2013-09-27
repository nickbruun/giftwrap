from base import *


class FileRule(Rule):
    """File rule.

    Copies a single file into the target.

    :ivar user: default `root`, Username to execute an application as.
    :ivar group: default ``None``, Group name to execute an application under.
    """

    def __init__(self, 
                 source_path,
                 destination_path,
                 user = None,
                 group = None,
                 permissions = None):
        """Initialize a file rule.

        :param source_path: Source path.
        :param destination_path: Destination path.
        :param user: default `root`, Username.
        :param group: default ``None``, Group name.
        """

        self.source_path = source_path
        self.destination_path = destination_path
        self.user = user
        self.group = group
        self.permissions = permissions


    def apply(self, package, context):
        import glob, os, fnmatch, shutil, stat

        # Create the destination directory if it does not exist.
        destination_dir = context.data_dir_path(
            os.path.dirname(self.destination_path)
        )
        destination_path = os.path.join(
            destination_dir,
            os.path.basename(self.destination_path)
        )

        # Copy the file.
        shutil.copyfile(self.source_path, destination_path)

        os.chmod(destination_path,
                 self.permissions if self.permissions is not None else
                 0755 if stat.S_IXUSR & os.stat(self.source_path)[stat.ST_MODE]
                 else 0644)
