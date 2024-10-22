#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2013 deanishe@deanishe.net.
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2013-11-01
#

"""workflow-build [options] <workflow-dir>

Build Alfred Workflows.

Compile contents of <workflow-dir> to a ZIP file (with extension
`.alfred3workflow`).

The name of the output file is generated from the workflow name,
which is extracted from the workflow's `info.plist`. If a `version`
file is contained within the workflow directory, it's contents
will be appended to the compiled workflow's filename.

Usage:
    workflow-build [-v|-q|-d] [-f] [-o <outputdir>] <workflow-dir>...
    workflow-build (-h|--version)

Options:
    -o, --output=<outputdir>    Directory to save workflow(s) to.
                                Default is current working directory.
    -f, --force                 Overwrite existing files.
    -h, --help                  Show this message and exit.
    -V, --version               Show version number and exit.
    -q, --quiet                 Only show errors and above.
    -v, --verbose               Show info messages and above.
    -d, --debug                 Show debug messages.

"""

from __future__ import print_function

import sys
import os
import logging
import logging.handlers
import plistlib
from subprocess import check_call, CalledProcessError

from docopt import docopt

__version__ = "0.4"
__author__ = "deanishe@deanishe.net"

DEFAULT_LOG_LEVEL = logging.WARNING
LOGPATH = os.path.expanduser('~/Library/Logs/MyScripts.log')
LOGSIZE = 1024 * 1024 * 5  # 5 megabytes


EXCLUDE_PATTERNS = [
    '*.pyc*',
    '*.log*',
    '.DS_Store',
    '*.acorn*',
    '*.swp*',
    '*.sublime-project*',
    '*.sublime-workflow*',
    '*.git*',
    '*.dist-info*',
    '*.egg-info*',
    '*.gif*',
    'README.md',
    'workflow-build.py',
    'requirements.txt',
    '*.idea*'
]


class TechnicolorFormatter(logging.Formatter):
    """
    Prepend level name to any message not level logging.INFO.

    Also, colour!

    """

    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

    RESET = "\033[0m"
    COLOUR_BASE = "\033[1;{:d}m"
    BOLD = "\033[1m"

    LEVEL_COLOURS = {
        logging.DEBUG: BLUE,
        logging.INFO: WHITE,
        logging.WARNING: YELLOW,
        logging.ERROR: MAGENTA,
        logging.CRITICAL: RED
    }

    def __init__(self, fmt=None, datefmt=None, technicolor=True):
        logging.Formatter.__init__(self, fmt, datefmt)
        self.technicolor = technicolor
        self._isatty = sys.stderr.isatty()

    def format(self, record):
        if record.levelno == logging.INFO:
            msg = logging.Formatter.format(self, record)
            return msg
        if self.technicolor and self._isatty:
            colour = self.LEVEL_COLOURS[record.levelno]
            bold = (False, True)[record.levelno > logging.INFO]
            levelname = self.colourise('{:9s}'.format(record.levelname),
                                       colour, bold)
        else:
            levelname = '{:9s}'.format(record.levelname)
        return (levelname + logging.Formatter.format(self, record))

    def colourise(self, text, colour, bold=False):
        colour = self.COLOUR_BASE.format(colour + 30)
        output = []
        if bold:
            output.append(self.BOLD)
        output.append(colour)
        output.append(text)
        output.append(self.RESET)
        return ''.join(output)


# logfile
logfile = logging.handlers.RotatingFileHandler(LOGPATH, maxBytes=LOGSIZE,
                                               backupCount=5)
formatter = logging.Formatter(
    '%(asctime)s %(levelname)-8s [%(name)-12s] %(message)s',
    datefmt="%d/%m %H:%M:%S")
logfile.setFormatter(formatter)
logfile.setLevel(logging.DEBUG)

# console output
console = logging.StreamHandler()
formatter = TechnicolorFormatter('%(message)s')
console.setFormatter(formatter)
console.setLevel(logging.DEBUG)

log = logging.getLogger('')
log.addHandler(logfile)
log.addHandler(console)


def safename(name):
    """Make name filesystem-safe."""
    name = name.replace(u'/', u'-')
    name = name.replace(u':', u'-')
    name = name.replace(u' ', u'-')
    return name


def build_workflow(workflow_dir, outputdir, overwrite=False, verbose=False):
    """Create an .alfred3workflow file from the contents of `workflow_dir`."""
    curdir = os.curdir
    os.chdir(workflow_dir)
    info = plistlib.readPlist(u'info.plist')
    version = None
    if not os.path.exists(u'info.plist'):
        log.error(u'info.plist not found')
        return False

    if 'version' in info and info.get('version'):
        version = info['version']
    elif os.path.exists(u'version'):
        with open('version') as fp:
            version = fp.read().strip().decode('utf-8')

    name = safename(info[u'name'])
    zippath = os.path.join(outputdir, name)
    if version:
        zippath += u'-' + version
    zippath += u'.alfred3workflow'

    if os.path.exists(zippath):
        if overwrite:
            log.info(u'Overwriting existing workflow')
            os.unlink(zippath)
        else:
            log.error(u"File '{}' already exists. Use -f to overwrite".format(
                      zippath))
            return False

    # build workflow
    command = [u'zip']
    if not verbose:
        command.append(u'-q')
    command.append(zippath)
    for root, dirnames, filenames in os.walk(u'.'):
        for filename in filenames:
            path = os.path.join(root, filename)
            command.append(path)
    command.append(u'-x')
    command.extend(EXCLUDE_PATTERNS)
    log.debug(u'command : {}'.format(u' '.join(command)))
    try:
        check_call(command)
    except CalledProcessError as err:
        log.error(u'zip returned : {}'.format(err.returncode))
        os.chdir(curdir)
        return False
    log.info(u'Wrote {}'.format(zippath))
    os.chdir(curdir)
    return True


def main(args=None):
    """Run CLI."""
    args = docopt(__doc__, version=__version__)

    if args.get('--verbose'):
        log.setLevel(logging.INFO)
    elif args.get('--quiet'):
        log.setLevel(logging.ERROR)
    elif args.get('--debug'):
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(DEFAULT_LOG_LEVEL)

    log.debug("Set log level to %s" %
              logging.getLevelName(log.level))

    log.debug('args :\n{}'.format(args))

    # Build options
    outputdir = os.path.abspath(args.get(u'--output') or os.curdir)
    workflow_dirs = [os.path.abspath(p) for p in args.get(u'<workflow-dir>')]
    log.debug(u'outputdir : {}, workflow_dirs : {}'.format(outputdir,
                                                           workflow_dirs))
    errors = False
    verbose = False
    if log.level == logging.DEBUG:
        verbose = True

    # Build workflow(s)
    for path in workflow_dirs:
        ok = build_workflow(path, outputdir, args.get(u'--force'), verbose)
        if not ok:
            errors = True
    if errors:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
