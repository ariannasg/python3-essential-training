#! usr/bin/env python3

# Str is a fundamental built-in type (all types are classes). Everything is an object in Python 3.
# Strings are immutable in python
z = 'seven'
print(z)
print('z is {}'.format(type(z)))

print('strings are objects so we can use their functions')
print(z.upper())

print('can have multi-line strings')
z = """
multi-line string
"""
print(z)

print('can create spaces or 0s using the format function')
z = 'seven {1} {0}'.format(8, 9)
print(z)

z = 'seven {1:>9} {0:>9}'.format(8, 9)
print(z)  # seven         9         8

z = 'seven {1:<9} {0:>9}'.format(8, 9)
print(z)  # seven 9                 8

z = 'seven "{1:<9}" "{0:>9}"'.format(8, 9)
print(z)  # seven "9        " "        8"

z = 'seven "{1:<09}" "{0:>09}"'.format(8, 9)
print(z)  # seven "900000000" "000000008" -> only works with  0, a letter will throw error and numbers will add spaces

za = 8
zb = 9
z = f'seven "{za:<09}" "{zb:>09}"'
print(z)  # seven "900000000" "000000008"

x = 42 * 74718
print('the number is "{}"'.format(x))
print('the number is "{:,}"'.format(x))  # format with commas for thousand separation
print('the number is "{:,}"'.format(x).replace(',', '.'))
print('the number is "{:f}"'.format(x))  # show decimal places
print('the number is "{:.3f}"'.format(x))  # show just 3 decimal places
print(f'the number is "{x:.3f}"')
print('the number is "{:,.2f}"'.format(x))  # format with commas and also show 2 decimal places
print(f'the number is "{x:,.2f}"')
print('the hex of 10 is "{:x}"'.format(10))  # put it in hexadecimal
print('the octal of 10 is "{:o}"'.format(10))  # put it in octal
print('the binary of 10 is "{:b}"'.format(10))  # put it in binary


class ReverseString(str):
    def __str__(self):
        return self[::-1]


print()
hello = ReverseString('Hello World')
print(hello)

print('\nCommon string object methods')
print('Hello, World.'.upper())
print('Hello, World.'.capitalize())
print('Hello, World.'.title())
print('Hello, World.'.swapcase())
print('Hello, World. ß'.lower())
print('Hello, World ß.'.casefold())  # similar to lower case but removes all case distinctions in unicode
print()
s1 = 'Hello, World.'
s2 = s1.upper()
print(id(s1))
print(id(s2))
print('\nconcatenation')
s3 = 'Another string'
print(s1 + s3)
print('one string ' 'and another string')

print("\nSplitting and joining")
x = 'This is a string with a bunch of words in it'
print(x.split())
print(x.split('i'))
s = x.split()
s2 = ':'.join(s)
print(s2)
print(x.replace(' ', ':'))

print("\nSome string built-in functions")
s = 'Hello World'
print(repr(s))  # prints the best possible string representation of an object


class Bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'The number of bunnies is: {self._n} 🖖'

    def __str__(self):
        return f'Number of bunnies: {self._n}'


x = Bunny(3)
print(repr(x))
print(x)
print(ascii(x))  # works just like repr but escaping chars
print(ord('🖖'))  # the opposite of chr - gives the number of a character
print(chr(128406))  # this function prints the character represented by that unicode precision

# CONSOLE OUTPUT:
# seven
# z is <class 'str'>
# strings are objects so we can use their functions
# SEVEN
# can have multi-line strings
#
# multi-line string
#
# can create spaces or 0s using the format function
# seven 9 8
# seven         9         8
# seven 9                 8
# seven "9        " "        8"
# seven "900000000" "000000008"
# seven "800000000" "000000009"
# the number is "3138156"
# the number is "3,138,156"
# the number is "3.138.156"
# the number is "3138156.000000"
# the number is "3138156.000"
# the number is "3138156.000"
# the number is "3,138,156.00"
# the number is "3,138,156.00"
# the hex of 10 is "a"
# the octal of 10 is "12"
# the binary of 10 is "1010"
#
# dlroW olleH
#
# Common string object methods
# HELLO, WORLD.
# Hello, world.
# Hello, World.
# hELLO, wORLD.
# hello, world. ß
# hello, world ss.
#
# 4400069488
# 4400153904
#
# concatenation
# Hello, World.Another string
# one string and another string
#
# Splitting and joining
# ['This', 'is', 'a', 'string', 'with', 'a', 'bunch', 'of', 'words', 'in', 'it']
# ['Th', 's ', 's a str', 'ng w', 'th a bunch of words ', 'n ', 't']
# This:is:a:string:with:a:bunch:of:words:in:it
# This:is:a:string:with:a:bunch:of:words:in:it
#
# Some string built-in functions
# 'Hello World'
# The number of bunnies is: 3 🖖
# Number of bunnies: 3
# The number of bunnies is: 3 \U0001f596
# 128406
# 🖖
