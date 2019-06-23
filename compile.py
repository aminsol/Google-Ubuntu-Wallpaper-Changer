from py_compile import compile
from os import path

if __name__ == '__main__':
    destination = path.realpath(path.curdir)+'/WallpaperChanger.pyc'
    print('Destination: %s' % destination)
    compile('main.py', destination)
