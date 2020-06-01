#!usr/bin/env python3
import collections


# The collections module provides two interesting dictionary subclasses to
# help out with common scenarios where a regular dictionary would need
# unnecessary code. It's a common scenario to use dictionaries to keep track
# of data, such as the result of counting operations. Default dict can make
# our code simpler to read in this scenario.
# the factory object doesn't need to be a built-in class, like an int or a
# string, it could be any custom object that you want. we need to be careful
# when you using defaultdict, because any key that we didn't explicitly add to
# the dictionary, will be assigned a default value when we try to access it.
# So, if we have a situation where a key is missing from the dictionary, this
# is an important indicator that defaultdict is not the right collection to use
def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # Count the elements in the list in the traditional manner
    # I'll get "KeyError: 'apple'" if I don't add the key check
    fruit_counter = {}
    for fruit in fruits:
        if fruit in fruit_counter.keys():
            fruit_counter[fruit] += 1
        else:
            fruit_counter[fruit] = 1

    print_dict(fruit_counter)

    # use a defaultdict to count each element.
    print('with defaultdict')
    # we pass the integer class as the factory function which acts as the
    # creator of the default value.
    fruit_counter_2 = collections.defaultdict(int)
    for fruit in fruits:
        fruit_counter_2[fruit] += 1
    print_dict(fruit_counter_2)

    # I can define my own factory method too. If I wanted the initial value to
    # start off at a different level, I could just use a lambda function.
    print('with defaultdict using a lambda as the factory function')
    fruit_counter_3 = collections.defaultdict(lambda: 10)
    for fruit in fruits:
        fruit_counter_3[fruit] += 1
    print_dict(fruit_counter_3)


def print_dict(fruit_counter):
    for key, value in fruit_counter.items():
        print(key + ":", value)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# apple: 2
# pear: 1
# orange: 1
# banana: 3
# grape: 1
# with defaultdict
# apple: 2
# pear: 1
# orange: 1
# banana: 3
# grape: 1
# with defaultdict using a lambda as the factory function
# apple: 12
# pear: 11
# orange: 11
# banana: 13
# grape: 11
