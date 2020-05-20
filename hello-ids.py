#! usr/bin/env python3

x = (1, "two", [3, 'three'], 4)
y = (1, "two", [3, 'three'], 4)
print(f'x is {x}')
print(f'y is {y}')
print(type(x))
print(type(y))
print(id(x))
print(id(y))
print(type(x[2]))
print(type(y[2]))
print(id(x[0]))
print(id(y[0]))
print(id(x[1]))
print(id(y[1]))
print(id(x[2]))
print(id(y[2]))

if x[0] is y[0]:
    print('They are exactly the same object')

if isinstance(x, tuple):
    print('x is a tuple')
if isinstance(x[2], list):
    print('x[2] is a tuple')
if not isinstance(x[2], dict):
    print('x[2] is not a dictionary')

# CONSOLE OUTPUT:
# x is (1, 'two', [3, 'three'], 4)
# y is (1, 'two', [3, 'three'], 4)
# <class 'tuple'>
# <class 'tuple'>
# 4501633440
# 4502127776
# <class 'list'>
# <class 'list'>
# 4497001120
# 4497001120
# 4501647536
# 4501647536
# 4501650752
# 4501661568
# They are exactly the same object
# x is a tuple
# x[2] is a tuple
# x[2] is not a dictionary
