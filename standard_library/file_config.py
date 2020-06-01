#!usr/bin/env python3
import configparser

# Using configuration files is a simple way to store key value pairs of data,
# for use in your code without the complicated structure of JSON, and the
# config parser module makes it really easy to work with them.

# Create an instance of the ConfigParser object
parser = configparser.ConfigParser()

# Read the configuration file
parser.read("config.cfg")

# print the sections
print(parser.sections())
print(parser.has_section("Section 1"))

# Access one of the default values like if the parser was a dictionary
# attention! the parser treats all values as strings, so even though you
# can see that this value is the true keyword, it isn't parsed as a Boolean;
# we have to explicitly convert it to a boolean
using_time_travel = bool(parser['DEFAULT']['UseTimeTravel'])
print(using_time_travel)
print(type(using_time_travel))

# Demonstrate the getXXX convenience functions
# for avoiding the explicit conversion str to the adequate type of the config
# value, we use the convenience functions
opd = parser['DEFAULT'].getboolean('ObeyPrimeDirective')
print(opd)
speed = parser['DEFAULT'].getfloat('Ship Speed')
print(speed)
print(type(speed))

# Access a non-existent value
try:
    title = parser['Section 3']['Title']
    print(title)
except KeyError as err:
    print("Whoa! There is no ", err)

# CONSOLE OUTPUT:
# ['Section 1', 'Section 2']
# True
# True
# <class 'bool'>
# False
# 56324.586
# <class 'float'>
# Whoa! There is no  'Section 3'
