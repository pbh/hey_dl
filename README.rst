hey_dl
===============
Directory Localizer helps you localize directories.

__doc__
-------
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
