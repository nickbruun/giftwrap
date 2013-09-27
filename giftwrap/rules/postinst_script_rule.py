from base import *

class PostInstallScriptRule(Rule):
    """Post installation script rule.
    
    Allows the execution of one or more shell script lines after installation 
    has succeeded.
    """
    
    def __init__(self, 
                 script):
        """Initialize a post installation script rule.
        
        :param script: String or, preferably, list of strings containing the 
        lines of the script.
        """
        
        self._script = script if isinstance(script, list) else script.split('\n')
    
    
    def apply(self, package, context):
        context.postinst_commands += self._script
