#!usr/bin/env python3


# python is referred to as the the batteries included language, because it
# has a lot of functionality built into it.
# we should use the built-in functions when possible since they are implemented
# in the python runtime as native code.
def main():
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]

    # any will return true if any of the sequence values are true
    print('is any value true: ', any(list1))

    # all will return true only if all values are true
    print('are all values true: ', all(list1))

    # min and max will return minimum and maximum values in a sequence
    print('min: ', min(list1))
    print('max: ', max(list1))

    # Use sum() to sum up all of the values in a sequence
    print('sum: ', sum(list1))


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# True
# False
# min:  0
# max:  6
# sum:  17
