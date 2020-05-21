#!/usr/bin/env python3

import sys


def main():
    try:
        x = int('hello')
    except ValueError:
        print('Caught a ValueError')

    try:
        x = 5 / 0
    except ValueError:
        print('Caught a ValueError')
    except ZeroDivisionError:
        print('Caught a ZeroDivisionError')

    try:
        x = 5 / 1
    except ValueError:
        print('Caught a ValueError')
    except ZeroDivisionError:
        print('Caught a ZeroDivisionError')
    else:
        print('Good job')

    try:
        x = 5 / 0
    except ValueError:
        print('Caught a ValueError')
    except:
        print(f'unknown error {sys.exc_info()}')
    else:
        print('Good job')

    try:
        raise TypeError
    except TypeError:
        print('Raised and Caught a TypeError')


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# Caught a ValueError
# Caught a ZeroDivisionError
# Good job
# unknown error (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x107b94c00>)
# Raised and Caught a TypeError
