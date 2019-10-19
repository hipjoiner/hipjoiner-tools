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
    for dir in dirs:
        if not os.path.isdir(dir):
            continue
        files = os.listdir(dir)
        for fname in files:
            fpath = '%s\%s' % (dir, fname)
            if not os.path.isfile(fpath):
                continue
            if arg == fname.split('.')[0]:
                result.append(fpath)
    for path in result:
        print(path)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: which <term>')
        sys.exit(0)
    which(sys.argv[1])
