#! usr/bin/env python3

# Sequences are lists, tuples and dictionaries. They are fundamental built-in types (all types are classes).
# Everything is an object in Python 3.
# Try to use tuples instead of lists, unless you know the object will change.

x = [1, 2, 3, 4, 5]
for i in x:
    print('i is {}'.format(i))
print('Lists operations')
game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
print(game[1])
# slicing!! -> can be applied to strings
print(game[1:5], end=' ', flush=True)  # works like range()
print()
print(game[1:5:2], end=' ', flush=True)  # works like range()
print()
i = game.index('Paper')
print(game[i])
game.append('New Item')
print(game)
game.insert(0, 'New Item at the beginning')
print(game)
i = game.pop()  # remove by default last index and return it
print(i)
print(game)
del game[0]
print(game)
del game[0:3:2]  # works like range()
print(game)
print(', '.join(game))
print(len(game))

print('Lists are mutable')
x[2] = 42
for i in x:
    print('i is {}'.format(i))

print('''Tuples work like lists but they are immutable, if I try reassigning a value I will get an error. 
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

print('Dictionaries operations')
animals = dict(kitten='meow', puppy='ruff!', lion='grrr', giraffe='I am a giraffe!', dragon='rawr')
for k, v in animals.items():
    print(f'key: {k}, value: {v}')
for k in animals.keys():
    print(k)
for v in animals.values():
    print(v)
animals['lion'] = 'I am a lion'
print(animals)
animals['monkey'] = 'I am a monkey'
print(animals)
print('lion found' if 'lion' in animals else 'lion not found')
print('godzilla found' if 'godzilla' in animals else 'godzilla not found')
print(animals.get('godzilla'))

print('Sets are like lists that do not allow duplicate elements')
a = set("Hello John")
b = set("Hello Kate")
print(a)  # it comes at a different order each time I run it
print(b)  # it comes at a different order each time I run it
print(sorted(a))  # it will always print the same order
print(sorted(b))  # it will always print the same order
print(a - b)  # it will print diff order or elements that are in a but not in b
print(a | b)  # it will print diff order or all elements that are either in a, or b or in both (inclusive or)
print(a ^ b)  # it will print diff order or all elements that are in a or b but not both (exclusive or)
print(a & b)  # it will print diff order or all elements that are in both a and b

print('Container/collection functions')
x = (1, 2, 3, 4, 5)
y = list(reversed(x))
print(x)
print(y)
print(sum(x))
print(sum(x, 10))  # start in 10 and then add elements in x
print(max(x))
print(min(x))
print(any(x))  # returns true if any element is true
print(any((0, 0, 0, 0)))
print(all(x))  # returns true if all elements are true
print(all((0, 1, 1, 0)))
y = (6, 7, 8, 9, 10, 11, 12)
z = zip(x, y)  # return tuples of elements in both iterators
print(z)
for i in z:
    print(i, end=' ')
print()
x = ('cat', 'dog', 'rabbit', 'duck')
print(x)
for i, v in enumerate(x):
    print(f'i:{i}, v:{v}')

# CONSOLE OUTPUT:
# i is 1
# i is 2
# i is 3
# i is 4
# i is 5
# Lists operations
# Paper
# ['Paper', 'Scissors', 'Lizard', 'Spock']
# ['Paper', 'Lizard']
# Paper
# ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock', 'New Item']
# ['New Item at the beginning', 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock', 'New Item']
# New Item
# ['New Item at the beginning', 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
# ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
# ['Paper', 'Lizard', 'Spock']
# Paper, Lizard, Spock
# 3
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
# Dictionaries operations
# key: kitten, value: meow
# key: puppy, value: ruff!
# key: lion, value: grrr
# key: giraffe, value: I am a giraffe!
# key: dragon, value: rawr
# kitten
# puppy
# lion
# giraffe
# dragon
# meow
# ruff!
# grrr
# I am a giraffe!
# rawr
# {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'I am a lion', 'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}
# {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'I am a lion', 'giraffe': 'I am a giraffe!', 'dragon': 'rawr', 'monkey': 'I am a monkey'}
# lion found
# godzilla not found
# None
# Sets are like lists that do not allow duplicate elements
# {'e', 'J', 'l', 'n', ' ', 'o', 'H', 'h'}
# {'e', 'l', ' ', 't', 'a', 'o', 'H', 'K'}
# [' ', 'H', 'J', 'e', 'h', 'l', 'n', 'o']
# [' ', 'H', 'K', 'a', 'e', 'l', 'o', 't']
# {'n', 'J', 'h'}
# {'e', 'J', 'l', 'n', ' ', 't', 'o', 'K', 'H', 'a', 'h'}
# {'J', 'n', 't', 'a', 'K', 'h'}
# {'e', 'l', ' ', 'o', 'H'}
# Container/collection functions
# (1, 2, 3, 4, 5)
# [5, 4, 3, 2, 1]
# 15
# 25
# 5
# 1
# True
# False
# True
# False
# <zip object at 0x10a7eed80>
# (1, 6) (2, 7) (3, 8) (4, 9) (5, 10)
# ('cat', 'dog', 'rabbit', 'duck')
# i:0, v:cat
# i:1, v:dog
# i:2, v:rabbit
# i:3, v:duck
