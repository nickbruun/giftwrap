"""
Package priorities.
===================

Prorities as defined in
http://www.debian.org/doc/debian-policy/ch-archive.html#s-priorities
"""

PRIORITY_REQUIRED = 'required'
"""Package is necessary for the proper functioning of the system.
"""


PRIORITY_IMPORTANT = 'important'
"""Important package.

Like those containing programs which one would expect to find on any Unix-like
system.
"""


PRIORITY_STANDARD = 'standard'
"""Package provides a reasonably small but not too limited system.
"""


PRIORITY_OPTIONAL = 'optional'
"""Package is optional.
"""


PRIORITY_EXTRA = 'extra'
"""Package is likely to be useful in specific situations.
"""
