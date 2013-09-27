import re, datetime
from .priorities import PRIORITY_OPTIONAL
from .sections import SECTION_WEB
from .packaging_context import PackagingContext


PACKAGE_NAME_EXPRESSION = re.compile(r'[a-z0-9][a-z0-9\+\-\.]+')
"""Name validation expression.
"""


class Package(object):
    """Package.

    :ivar name:
        Package name. Must consist only of lower case letters (a-z),
        digits (0-9), plus (+) and minus (-) signs, and periods (.). They must
        be at least two characters long and must start with an alphanumeric
        character.
    :ivar maintainer_name: Package maintainer's name.
    :ivar maintainer_email: Package maintainer's e-mail address.
    :ivar homepage: Package homepage.
    :ivar description:
        Short, one-line description. Keep short and concise, and do not start
        with the package name.
    :ivar long_description:
        Longer description not starting with the package.
    name.
    :ivar version: Package version.
    :ivar depends: Dependencies of the package.
    :ivar architectures:
        Package architecture(s) as a list or tuple of architectures.
    :ivar section:
        Package section. Specifies an application area into which the package
        has been classified.
    :ivar priority: Package priority.
    :ivar copyright: Copyright/license text for the package.
    :ivar rules: Package rules.
    """

    def __init__(self, 
                 name,
                 maintainer_name, 
                 maintainer_email, 
                 homepage, 
                 description, 
                 long_description, 
                 version, 
                 depends = [], 
                 architectures = None, 
                 section = SECTION_WEB, 
                 priority = PRIORITY_OPTIONAL):
        """Initialize a new package representation.

        :ivar name:
            Package name. Must consist only of lower case letters (a-z), digits
            (0-9), plus (+) and minus (-) signs, and periods (.). They must be
            at least two characters long and must start with an alphanumeric
            character.
        :ivar maintainer_name: Package maintainer's name.
        :ivar maintainer_email: Package maintainer's e-mail address.
        :ivar homepage: Package homepage.
        :ivar description:
            Short, one-line description. Keep short and concise, and do not
            start with the package name.
        :ivar long_description:
            Longer description not starting with the package name.
        :ivar version: Package version.
        :param depends:
            default [], Packages on which the package depends as either a list
            or tuple.
        :param architecture:
            default ``None``, Package architecture(s) as a list or tuple of
            architectures. If ``None`` is supplied, the current system
            architecture will be used.
        :param section:
            default ``SECTION_WEB``, Package section. Specifies an application
            area into which the package has been classified.
        :param priority: default ``PRIORITY_OPTIONAL``, Package priority.
        """

        # Check the name.
        self.name = name.strip().lower()
        if not PACKAGE_NAME_EXPRESSION.match(self.name):
            raise ValueError('invalid package name -- package names must consist of only letters, digits, plus and minus signs, and periods. They must be at least two characters long and must start with an alphanumeric character.')

        # Check the maintainer.
        if not isinstance(maintainer_name, str):
            raise TypeError('maintainer name must be a string')
        self.maintainer_name = maintainer_name.strip()
        if len(self.maintainer_name) == 0:
            raise ValueError('maintainer name cannot be empty')

        if not isinstance(maintainer_email, str):
            raise TypeError('maintainer e-mail address must be a string')
        self.maintainer_email = maintainer_email.strip()
        if len(self.maintainer_email) == 0:
            raise ValueError('maintainer e-mail address cannot be empty')

        # Store.
        self.homepage = homepage
        self.description = description
        self.long_description = long_description
        self.version = version
        self.depends = depends
        self.architectures = architectures
        self.section = section
        self.priority = priority

        # Reset other controlling variables.
        self.copyright = 'Copyright %d %s <%s>' % (
            datetime.datetime.utcnow().year, 
            self.maintainer_name, 
            self.maintainer_email
        )
        
        # Initialize an empty rule set.
        self.rules = []

    def pack(self, destination_path, run_lintian = False):
        """Pack the representation to a Debian package.

        :param destination_path: Destination of the created package.
        :param run_lintian: default ``False``, whether or not to run Lintian 
        to check the package after the package has been generated. If Lintian 
        is not found, this parameter will be ignored.
        """

        context = PackagingContext()
        context.build(self)
        context.pack(self, destination_path, run_lintian)

    def add_dependency(self, dependency):
        """Add a dependency.

        :param dependency: Dependency name.
        """

        if not dependency in self.depends:
            self.depends.append(dependency)

    def add_rule(self, rule):
        """Add a rule to the package.

        :param rule: Rule to add.
        """

        self.rules.append(rule)
