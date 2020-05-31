#! usr/bin/env python3

from decimal import *

# Numeric types int and float are fundamental built-in types (all types are classes).
# Everything is an object in Python 3.
x = 7
print(x)
print('x is type {}'.format(type(x)))

print(x / 3)
print(x // 3)  # 2 -> removes the remainder of 7/2
print(x % 3)  # 1 -> just the remainder of 7/2

# Floating numbers have precision but not accuracy
print(.10 + .10 + .10 - .30)  # 5.551115123125783e-17 -> DO NOT USE FLOATING POINTS FOR MONEY OPERATIONS!
a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print(x)  # 0.00
print(type(x))

x = int(47.3)
y = abs(x)
print(f'y is {y}')
print(f'y is {type(y)}')

x = float(47.3)
y = abs(x)
print(f'y is {y}')
print(f'y is {type(y)}')

x = 31
y = divmod(x, 3)  # returns tuple of the division and the remainder
print(f'y is {y}')
print(f'y is {type(y)}')


x = 47
y = complex(x, 3)  # returns tuple of the division and the remainder
print(f'y is {y}')
print(f'y is {type(y)}')

# CONSOLE OUTPUT:
# 7
# x is type <class 'int'>
# 2.3333333333333335
# 2
# 1
# 5.551115123125783e-17
# 0.00
# <class 'decimal.Decimal'>
# y is 47
# y is <class 'int'>
# y is 47.3
# y is <class 'float'>
# y is (10, 1)
# y is <class 'tuple'>
# y is (47+3j)
# y is <class 'complex'>
