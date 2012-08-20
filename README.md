# Python library for packaging Debian packages the way I like it.

## Example

    pkg = Package(name = 'testy',
                  maintainer_name = 'Nick Bruun', 
                  maintainer_email = 'nick@bruun.co', 
                  homepage = 'http://bruun.co/', 
                  description = 'Short description', 
                  long_description = 'Loooooooooong description. More and more and more',
                  version = '1.0.5')
    pkg.add_rule(UserRule('testy', 'web'))
    pkg.add_rule(RunItRule('testy-api', 
                           ['/usr/bin/testy'], 
                           user = 'testy', 
                           group = 'web'))
    pkg.add_rule(GlobRule('/usr/src/testy/build/bin', 
                          '/usr/bin', 
                          ignore = ['venv', '.git*', '*.pyc']))
    pkg.pack('/tmp/testy.deb', 
             True)
