from utilities import string_ending_in_period, run


class ControlFileGenerator(object):
    """Package control file generator.

    Generates a control file for a package, as located in `control/control`.
    Follows the documentation of
    http://www.debian.org/doc/debian-policy/ch-controlfields.html
    as closely as possible.
    """

    def generate(self, package, output_path, control_binary=True):
        """Generate a control file.

        :param output_path: Fully qualified output path.
        :param control_binary:
            default ``True``, Whether or not the generated file should
            represent a binary package. If ``False``, the control file will be
            for a source distribution package.
        """

        # Determine the architecture.
        if isinstance(package.architectures, list):
            architectures = package.architectures
        elif isinstance(package.architectures, tuple):
            architectures = list(package.architectures)
        elif isinstance(package.architectures, str):
            architectures = [package.architectures]
        else:
            # Hacky but it works for now.
            host_architecture = run(['dpkg', '--print-architecture'],
                                    vital=False)
            architectures = [
                host_architecture.strip()
                if host_architecture is not None else 'any'
            ]

        if not control_binary and 'source' not in architectures:
            architectures.append('source')

        # Build the rules set based on availability.
        rules = {
            'Source': package.name,
            'Version': package.version,
            'Architecture': ' '.join(architectures),
            'Maintainer': '%s <%s>' % (package.maintainer_name,
                                       package.maintainer_email),
            'Description': '%s\n %s' % (
                string_ending_in_period(package.description),
                string_ending_in_period(package.long_description)
            )
        }

        if package.homepage is not None:
            rules['Homepage'] = package.homepage

        if control_binary:
            rules['Package'] = package.name

        if package.section is not None:
            rules['Section'] = package.section

        if package.priority is not None:
            rules['Priority'] = package.priority

        if package.depends is not None and len(package.depends) > 0:
            rules['Depends'] = ' '.join(package.depends)

        # Finally, write the file.
        with open(output_path, 'w') as output_file:
            output_file.write(
                ''.join(['%s: %s\n' % (k, rules[k]) for k in rules])
            )
            output_file.close()
