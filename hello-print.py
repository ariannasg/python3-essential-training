#! usr/bin/env python3

x = 42

print('Hello world using python 2 style (deprecated). %d' % x)
print('Hello world using python 3 style. {}'.format(x))
print(f'Hello world using the f function. {x}. "f strings" are only available on python 3.6 onwards.')

# CONSOLE OUTPUT:
# Hello world using python 2 style (deprecated). 42
# Hello world using python 3 style. 42
# Hello world using the f function. 42. "f strings" are only available on python 3.6 onwards.
