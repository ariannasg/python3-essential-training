#!usr/bin/env python3
import string

# use predefined string constants
# predefined string constants can be used in common scenarios
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)

# Use the constants to filter information out
test_string1 = "The quick brown fox jumps over the lazy dog on the 1st of Dec"
test_string2 = "Supercalifragilistic"
test_string3 = "90210"

result = "".join([c for c in test_string1 if c in string.ascii_letters])
print(result)

# String testing methods
# returns false because the space is not considered alpha-numeric
print(test_string1.isalnum())
# returns true because all chars in test_string2 are considered alphabetic strs
print(test_string2.isalpha())

print(any([c.isalpha() for c in test_string1]))

print(test_string3.isnumeric())

# CONSOLE OUTPUT:
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# 0123456789
# 0123456789abcdefABCDEF
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# ThequickbrownfoxjumpsoverthelazydogonthestofDec
# False
# True
# True
# True
