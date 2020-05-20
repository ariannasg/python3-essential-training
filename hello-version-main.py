#! usr/bin/env python3

import platform


def message():
    print('This is python version {}'.format(platform.python_version()))


def main():
    message()


if __name__ == '__main__':
    main()
