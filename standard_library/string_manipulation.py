#!usr/bin/env python3

# Working with string manipulation functions
test_string1 = "The quick brown fox jumps over the lazy dog on the 1st of Dec"

# upper and lower convert between cases
print(test_string1.upper())
print(test_string1.lower())

# Use the split and join functions to create a list of the words in the string,
# using the space as the delimiter
result = test_string1.split(" ")
print(result)
# Concatenate the strings in the list using a comma and a space as separator
letters = ["a", "b", "c", "d", "e"]
print(", ".join(letters))

# use justification functions to align strings and format the output
# ljust, center, rjust
names = ["Amy", "John", "George", "Michael", "Penelope"]
biggest = max(len(name) for name in names)

# left justify the str using a filling character
for name in names:
    print(name.ljust(biggest + 2, "-") + ":")
print()
# center justify the str using a filling character
for name in names:
    print(name.center(biggest + 2, "-") + ":")
print()
# right justify the str using a filling character
for name in names:
    print(name.rjust(biggest + 2, "-") + ":")

# left justify the str without using a filling character
print()
for name in names:
    print(name.ljust(biggest) + ":")
print()
# center justify the str without using a filling character
for name in names:
    print(name.center(biggest) + ":")
print()
# right justify the str without using a filling character
for name in names:
    print(name.rjust(biggest) + ":")

# Use a translation table to replace characters
# Python provides a way of performing batch replacement of characters in a
# string called a translation table.
# this example translates ordinary text into what's called leet speak where
# common letters are replaced by numbers.
sample_str = "The quick brown fox jumped over the lazy dog"

trans_table = str.maketrans("abegilostz", "4636110572")
print(trans_table)
print(sample_str)
print(sample_str.translate(trans_table))


# CONSOLE OUTPUT:
# THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG ON THE 1ST OF DEC
# the quick brown fox jumps over the lazy dog on the 1st of dec
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', 'on', 'the', '1st', 'of', 'Dec']
# a, b, c, d, e
# Amy-------:
# John------:
# George----:
# Michael---:
# Penelope--:
#
# ---Amy----:
# ---John---:
# --George--:
# -Michael--:
# -Penelope-:
#
# -------Amy:
# ------John:
# ----George:
# ---Michael:
# --Penelope:
#
# Amy     :
# John    :
# George  :
# Michael :
# Penelope:
#
#   Amy   :
#   John  :
#  George :
# Michael :
# Penelope:
#
#      Amy:
#     John:
#   George:
#  Michael:
# Penelope:
# {97: 52, 98: 54, 101: 51, 103: 54, 105: 49, 108: 49, 111: 48, 115: 53, 116: 55, 122: 50}
# The quick brown fox jumped over the lazy dog
# Th3 qu1ck 6r0wn f0x jump3d 0v3r 7h3 142y d06
