import os
import sys


def which(arg=None):
    if arg is None:
        if len(sys.argv) < 2:
            print('Usage: which <term>')
            sys.exit(0)
        arg = sys.argv[1]
    result = []
    dirs = os.environ['PATH'].split(os.pathsep)
    for d in dirs:
        d = d.rstrip(os.path.sep)
        if not os.path.isdir(d):
            continue
        files = os.listdir(d)
        for fname in files:
            fpath = '%s\%s' % (d, fname)
            if not os.path.isfile(fpath):
                continue
            if arg == fname.split('.')[0]:
                result.append(fpath)
    for path in result:
        print(path)


if __name__ == '__main__':
    which('ppath')
    """
    if len(sys.argv) < 2:
        print('Usage: which <term>')
        sys.exit(0)
    which(sys.argv[1])
    """