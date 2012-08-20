from base import *

class UserRule(Rule):
    """User rule.
    
    Ensures that a user is created and set up.
    
    :ivar user: default `root`, Username to execute an application as.
    :ivar group: default ``None``, Group name to execute an application under.
    :ivar system_user: default ``True``, System user.
    :ivar no_home_directory: default ``True``, No home directory.
    """
    
    def __init__(self, 
                 user, 
                 group = None, 
                 system_user = True, 
                 no_home_directory = True):
        """Initialize a user rule.
        
        :param user: default `root`, Username.
        :param group: default ``None``, Group name.
        :param system_user: default ``True``, System user.
        :param no_home_directory: default ``True``, No home directory.
        """
        
        self.user = user
        self.group = group
        self.system_user = system_user
        self.no_home_directory = no_home_directory
    
    
    def apply(self, 
              package, 
              context):
        
        package.add_dependency('adduser')

        context.postinst_commands += \
            ['if ! grep -q %s /etc/passwd; then' % (self.user), 
             '    adduser %s%s%s' % ('--system ' if self.system_user else '', 
                                     '--no-create-home ' if self.no_home_directory else '', 
                                     self.user)]
        
        if self.group != None:
            context.postinst_commands += \
                ['    addgroup %s%s' % ('--system ' if self.system_user else '', 
                                        self.group), 
                 '    adduser %s %s' % (self.user,
                                        self.group)]
        
        context.postinst_commands += ['fi']
