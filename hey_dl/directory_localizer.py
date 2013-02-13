#!/usr/bin/env python

"""
    hey_dl.directory_localizer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Utilities for working with the directory where a source file lives.

    :copyright: (c) 2013 by oDesk Corporation.
    :license: BSD, see LICENSE for more details.
"""

import os
import inspect

class DirectoryLocalizer(object):
    """
    Locate the directory of a file.

    Periodically, you'll want to know where a Python source file is actually
    located on disk.  You might want this for all sorts of reasons, and it's
    always a bit messy when you do want to know.

    DirectoryLocalizer solves two problems:
        1. it lets you know where you are on disk, assuming you're not
        anywhere crazy, like in a zip import, and
        2. it lets you pass that location to other code that might want
        to know where you are.

    Usage is extremely simple:
        1. Make a DirectoryLocalizer object, dl (or whatever).
        2. Call dl.set() from the file you want to locate on disk.
        3. Any code that can access dl can now call:
            dl.dir(): for the directory of the file where dl.set()
            was called,
            dl.path(fn): for the filename of a file in the directory
            where dl.set() was called,
            dl.file(fn): for a file object of the file in dl.path(fn), and
            dl.read(fn): to get a read of the file in d.file(fn).
    """

    def __init__(self):
        self._my_dir = None

    def set(self):
        "Set location to the calling file's location."
        s = inspect.stack()

        self._my_dir = os.path.abspath(
            os.path.join(os.path.abspath(
                    os.path.split(
                        inspect.getfile(s[1][0])         
                        )[0]),
                         './'))

    def dir(self):
        "Get dir of last Python source file where set() was called."
        return self._my_dir

    def path(self, filename):
        "Get self.dir() with filename appended."
        return os.path.join(self._my_dir, filename)

    def file(self, filename):
        "Get a file object for self.path(fn)."
        return file(self.path(filename))

    def read(self, filename):
        "Do a read of the file object self.file(fn)."
        return self.file(filename).read()

