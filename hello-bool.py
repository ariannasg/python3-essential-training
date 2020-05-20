#! usr/bin/env python3

# The bool type is a fundamental built-in type (all types are classes). Everything is an object in Python 3.

x = True
print(x)
print('x is {}'.format(type(x)))
x = 7 < 5
print(x)
print(type(x))

x = None
print(x)
print('x is {}'.format(type(x)))
if x:
    print('True')
else:
    print('False')

x = 0
print(x)
print('x is {}'.format(type(x)))
if x:
    print('True')
else:
    print('False')

x = ""
print(x)
print('x is {}'.format(type(x)))
if x:
    print('True')
else:
    print('False')

# CONSOLE OUTPUT:
# True
# x is <class 'bool'>
# False
# <class 'bool'>
# None
# x is <class 'NoneType'>
# False
# 0
# x is <class 'int'>
# False
#
# x is <class 'str'>
# False
