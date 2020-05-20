#! usr/bin/env python3

# Sequences are lists, tuples and dictionaries. They are fundamental built-in types (all types are classes).
# Everything is an object in Python 3.

x = [1, 2, 3, 4, 5]
for i in x:
    print('i is {}'.format(i))

print('Lists are mutable')
x[2] = 42
for i in x:
    print('i is {}'.format(i))

print('''Tuples are immutable, if I try reassigning a value I will get an error. 
Try to use tuples by default unless I know I need to change a value at some point''')
x = (1, 2, 3, 4, 5)
for i in x:
    print('i is {}'.format(i))

print('Tuples are immutable, if I try reassigning a value I will get an error')
x = (1, 2, 3, 4, 5)
for i in x:
    print('i is {}'.format(i))

print('Range is immutable, if I try reassigning a value I will get an error')
print('Can create a sequence using range; using one param as the end mark.')
x = range(5)
for i in x:
    print('i is {}'.format(i))
print('Can create a sequence using range; using two params: as the start and end marks')
x = range(5, 10)
for i in x:
    print('i is {}'.format(i))
print('Can create a sequence using range; using 3 params: as the start and end marks, plus a step by mark')
x = range(5, 50, 10)
for i in x:
    print('i is {}'.format(i))

print('Dictionaries is a sequence of key value pairs. Keys and values can be any type.')
x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for i in x:
    print('i is {}'.format(i))
for key, value in x.items():
    print('k: {}, v: {}'.format(key, value))
print('Dictionaries are mutable.')
x['three'] = 42
for key, value in x.items():
    print('k: {}, v: {}'.format(key, value))

# CONSOLE OUTPUT:
# i is 1
# i is 2
# i is 3
# i is 4
# i is 5
# Lists are mutable
# i is 1
# i is 2
# i is 42
# i is 4
# i is 5
# Tuples are immutable, if I try reassigning a value I will get an error.
# Try to use tuples by default unless I know I need to change a value at some point
# i is 1
# i is 2
# i is 3
# i is 4
# i is 5
# Tuples are immutable, if I try reassigning a value I will get an error
# i is 1
# i is 2
# i is 3
# i is 4
# i is 5
# Range is immutable, if I try reassigning a value I will get an error
# Can create a sequence using range; using one param as the end mark.
# i is 0
# i is 1
# i is 2
# i is 3
# i is 4
# Can create a sequence using range; using two params: as the start and end marks
# i is 5
# i is 6
# i is 7
# i is 8
# i is 9
# Can create a sequence using range; using 3 params: as the start and end marks, plus a step by mark
# i is 5
# i is 15
# i is 25
# i is 35
# i is 45
# Dictionaries is a sequence of key value pairs. Keys and values can be any type.
# i is one
# i is two
# i is three
# i is four
# i is five
# k: one, v: 1
# k: two, v: 2
# k: three, v: 3
# k: four, v: 4
# k: five, v: 5
# Dictionaries are mutable.
# k: one, v: 1
# k: two, v: 2
# k: three, v: 42
# k: four, v: 4
# k: five, v: 5
