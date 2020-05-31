#!usr/bin/env python3


# python functions support variable argument list, which makes possible to
# have functions with a high degree of flexibility by accepting different
# numbers of parameters.
# the potential drawback of using variable argument lists is that if we decide
# later to change the function signature to add more positional parameters then
# all of the callers of the function will have to change.
# variable argument lists are useful when the number of parameters are
# relatively small and we know they are unlikely to change
def main():
    # pass different arguments
    print(addition(5, 10, 15, 20))
    print(addition(1, 2, 3))
    print(addition(1, 2))
    print(addition(1))

    # pass an existing list
    my_nums = [5, 10, 15, 20]
    print(addition(*my_nums))


# define a function that takes variable arguments.
# naming the params as args is a convention within the python community
def addition(*args):
    result = 0
    for arg in args:
        result += arg

    return result


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# 50
# 6
# 3
# 1
# 50
