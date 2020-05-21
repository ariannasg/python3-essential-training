#! usr/bin/env python3

# Str is a fundamental built-in type (all types are classes). Everything is an object in Python 3.
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


class ReverseString(str):
    def __str__(self):
        return self[::-1]


print()
hello = ReverseString('Hello World')
print(hello)

# CONSOLE OUTPUT:
# seven
# z is <class 'str'>
# strings are objects
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
#
# dlroW olleH
