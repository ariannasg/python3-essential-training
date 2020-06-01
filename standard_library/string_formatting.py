#!usr/bin/env python3
import datetime
from string import Template

# We can format strings by using the format function, using template strings
# and using string interpolation.

# Using Template strings
the_str = "The quick brown $animal $action over the lazy dog"
the_template = Template(the_str)
output_str = the_template.substitute(animal="fox", action="jumped")
print(output_str)

args = {
    "animal": "cow",
    "action": "walked"
}
output_str = the_template.substitute(args)
print(output_str)

# Using str.format()
print("Output: {}, {}".format("foo", 123))
print("Output: {1}, {0}".format("foo", 123))
print("Output: {var2}, {var1}".format(var1="foo", var2=123))
# format with lowercase hexadecimal and uppercase hexadecimal
print("Output: {var2:x}, {var2:X}, {var1}".format(var1="foo", var2=123))

# Using interpolation with f-strings in Python 3.6
# the string interpolation function is invoked by using f at the beg.
# it allows to use variables and functions directly inside the formatted strs
product = "Widget"
price = 19.99
tax = 0.07
nyd = datetime.datetime(2019, 1, 1)
print(f"{product} has a price of {price}, with tax {tax:.2%} "
      f"the total is {round(price + (price * tax), 2)}")
print(f"But only on: {nyd:%B %d, %Y}")

# CONSOLE OUTPUT:
# The quick brown fox jumped over the lazy dog
# The quick brown cow walked over the lazy dog
# Output: foo, 123
# Output: 123, foo
# Output: 123, foo
# Output: 7b, 7B, foo
# Widget has a price of 19.99, with tax 7.00% the total is 21.39
# But only on: January 01, 2019
