from package import *
from rules import *

if __name__ == '__main__':
    oink = Package(name = 'testy',
                   maintainer_name = 'Nick Bruun', 
                   maintainer_email = 'nick@bruun.co', 
                   homepage = 'http://bruun.co/', 
                   description = 'Short description', 
                   long_description = 'Loooooooooong description. More and more and more',
                   version = '1.0.5')
    oink.add_rule(UserRule('analytics', 'web'))
    oink.add_rule(RunItRule('analytics-reporter', 
                            ['/usr/bin/visualanalytics-api'], 
                            user = 'analytics', 
                            group = 'web'))
    oink.add_rule(GlobRule('/home/nick/giftwrap', 
                           '/usr/local/hest', 
                           ignore = ['venv', '.git*', '*.pyc']))
    oink.pack('/tmp/oink.deb', 
              True)
