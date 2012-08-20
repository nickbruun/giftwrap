class RuleError(object):
    """Rule exception.
    """


class Rule(object):
    """Base rule.
    
    """
    
    
    def apply(self, 
              package, 
              context):
        """Apply the rule.
        
        :param package: Package.
        :param context: Packaging context.
        """
        
        raise RuleError('rule not implemented')
