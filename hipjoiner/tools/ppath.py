import os


def pretty_path():
    for d in os.getenv('PATH').split(os.pathsep):
        print(d)


if __name__ == '__main__':
    pretty_path()
