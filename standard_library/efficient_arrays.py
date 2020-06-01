#!usr/bin/env python3
from array import array

# The arrays feature allows us to create arrays that are limited to a specific
# type of data by using the array module.
# The array type can hold homogeneous data types and operate
# on them more efficiently while using less memory.
# we should use the arrays feature if we have a need to operate on uniform data
# sets (all data is of the same type) and we want some automatic enforcement
# of the type rules.

# Create an array of integer numbers
arr1 = array('i', [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
print(arr1.typecode)
print("Array 1 item size: ", arr1.itemsize)  # this is 4 bytes integers
print(arr1)

# Add additional items to the array
arr1.insert(2, 5)
print(arr1)
arr1.insert(0, 1)
print(arr1)
arr1.append(22)
print(arr1)
arr1.extend([24, 26, 28])
print(arr1)

# iterate over the array content like with any other list
for i, elem in enumerate(arr1):
    arr1[i] = elem * 2
print(arr1)

# Try to add a non-integer number to the array and will get an error:
# TypeError: integer argument expected, got float
# arr1.insert(0, 1.25)

# Create an array to hold bytes instead of ints
arr2 = array('B', [18, 102, 182, 56, 89, 5, 254, 32, 64, 50])
print(arr2.typecode)
print("Array 2 item size: ", arr2.itemsize)

# bytes can only hold values from 0 to 255
# so when we try to add an item that's out of range and will get an error:
# OverflowError: unsigned byte integer is greater than maximum
# arr2.append(300)

# Convert an array to a list
print(arr2.tolist())

# CONSOLE OUTPUT:
# i
# Array 1 item size:  4
# array('i', [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
# array('i', [2, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20])
# array('i', [1, 2, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20])
# array('i', [1, 2, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22])
# array('i', [1, 2, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])
# array('i', [2, 4, 8, 10, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56])
# B
# Array 2 item size:  1
# [18, 102, 182, 56, 89, 5, 254, 32, 64, 50]
