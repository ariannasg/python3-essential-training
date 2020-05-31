#!usr/bin/env python3
import collections


def main():
    print(map.__doc__, end="\n=====\n")
    print(collections.__doc__, end="\n=====\n")
    print(my_function.__doc__)


def my_function(arg1, arg2=None):
    """my_function(arg1, arg2=None) --> Doesn't really do anything special.

    :param arg1: the first argument.
    :param arg2: the second argument. Defaults to None
    """
    print(arg1, arg2)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# map(func, *iterables) --> map object
#
# Make an iterator that computes the function using arguments from
# each of the iterables.  Stops when the shortest iterable is exhausted.
# =====
# This module implements specialized container datatypes providing
# alternatives to Python's general purpose built-in containers, dict,
# list, set, and tuple.
#
# * namedtuple   factory function for creating tuple subclasses with named fields
# * deque        list-like container with fast appends and pops on either end
# * ChainMap     dict-like class for creating a single view of multiple mappings
# * Counter      dict subclass for counting hashable objects
# * OrderedDict  dict subclass that remembers the order entries were added
# * defaultdict  dict subclass that calls a factory function to supply missing values
# * UserDict     wrapper around dictionary objects for easier dict subclassing
# * UserList     wrapper around list objects for easier list subclassing
# * UserString   wrapper around string objects for easier string subclassing
# =====
# my_function(arg1, arg2=None) --> Doesn't really do anything special.
#
#     :param arg1: the first argument.
#     :param arg2: the second argument. Defaults to None
