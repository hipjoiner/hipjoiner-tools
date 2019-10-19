import os
import sys

if __name__ == '__main__':
    def resolve_module(mod_name):
        """Figure out where our enclosing package is, and add to search path.
        Why?  Because if this file is called as a script (rather than as a module), internal package references
        in code (e.g., import jwp.<etc>) won't work, unless we find the package dir, and add it to the search path.
        """
        path = os.path.dirname(os.path.join(os.getcwd(), __file__))
        tail = None
        while path and (tail != mod_name):
            path, tail = os.path.split(path)
        if tail != mod_name:
            raise SystemError('%s module directory not found; abort.' % mod_name)
        if path not in sys.path:
            sys.path.insert(0, path)
    resolve_module('jwp')

# Test above resolution logic by importing something in this package
from hipjoiner.tools.ppath import pretty_path


if __name__ == '__main__':
    pretty_path()
