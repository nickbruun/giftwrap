import os
import sys
import subprocess
import glob
import errno


def string_ending_in_period(input):
    """Make sure a string ends with a period.

    :param input: Input string.
    :returns: a :class:`str` ensured to end in a period.
    """

    input = input.strip()
    if len(input) == 0:
        return input

    return '%s%s' % (input, '.' if input[-1] != '.' else '')


def write_to_file(content, path, permissions=0o644):
    """Write the contents of a string to a given path.

    :param content: File content.
    :param path: File output path.
    :param permissions: File permissions.
    """

    with open(path, 'w') as output_file:
        output_file.write(content)
        output_file.close()

    os.chmod(path, permissions)


def write_lines_to_file(lines,
                        path,
                        permissions=0o644,
                        ending_newline=True):
    """Write the contents of a string to a given path.

    :param lines: Text lines.
    :param path: File output path.
    :param ending_newline: Whether or not the file should have an ending
    newline.
    :param permissions: File permissions.
    """

    with open(path, 'w') as output_file:
        output_file.write('%s%s' % ('\n' . join(lines),
                                    '\n' if ending_newline else ''))
        output_file.close()

    os.chmod(path, permissions)


def run(args, cwd=None, vital=True):
    """Run a command.

    :param args: Arguments of the command.
    :param cwd: Current working directory for executing the command.
    :param fatal:
        Whether or not successful execution is vital for the command.
        If execution fails for a vital command, a :class:`CalledProcessError`.
        exception will be raised.
    :returns: the output from the command on success, otherwise ``None``.
    """

    proc = subprocess.Popen(args,
                            cwd=cwd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    if ((vital) and
            (proc.returncode != 0)):
        print >> sys.stderr, stdout, stderr
        raise subprocess.CalledProcessError(proc.returncode,
                                            args[0],
                                            output=stderr)

    return stdout if proc.returncode == 0 else None


def ar_create(path,
              files,
              verbose=True):
    """Create an archive.

    Invokes the `ar` tool for archival operations.

    :param path: Output path of the archive.
    :param files: Files to add to the archive.
    """

    run(['ar',
         'rcv',
         path] + (files if isinstance(files, (list, tuple, )) else [files]))


def targz(path,
          cwd,
          files):
    """Package a given set of files to a gzipped tarball.

    :param path: Output path of the tarball.
    :param cwd: Working directory to pack the files from.
    :param files: Files to add to the archive.
    """

    abs_paths = files if isinstance(files, (list, tuple, )) else [files]
    rel_paths = [os.path.relpath(p, cwd) for p in abs_paths]

    run(['fakeroot', '--', 'tar', '-zvcf', path] + rel_paths,
        cwd=cwd)


def glob_dir(directory,
             expression='*'):
    """List all files in a directory matching a wildcard expression.

    :param directory: Directory path.
    :param expression: Expression to match files against.
    """

    return glob.glob(os.path.join(directory,
                                  expression))


def stringify_args(args):
    """Stringify arguments.

    :param args: Arguments to stringify.
    """

    args_strings = []

    for a in args:
        contains_whitespace = ((' ' in a) or
                               ('\t' in a) or
                               ('\r' in a) or
                               ('\n') in a)
        contains_quotes = ('"' in a)

        if contains_quotes:
            a = a.replace('\\', '\\\\').replace('"', '\\"')

        if contains_whitespace:
            a = '"%s"' % (a)

        args_strings.append(a)

    return ' '.join(args_strings)


def mkdirp(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST:
            pass
        else:
            raise
