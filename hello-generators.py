#!usr/bin/env python3


# A generator function serves as an iterator, instead of returning a single value, returns a stream of values
def main():
    for i in inclusive_range(25):
        print(i, end=' ')
    print()
    for i in inclusive_range(5, 25):
        print(i, end=' ')
    print()
    for i in inclusive_range(5, 25, 10):
        print(i, end=' ')
    print()


# my inclusive_range is like the range function, but including the last number
def inclusive_range(*args):
    num_args = len(args)
    start = 0
    step = 1

    # initialize parameters that describe the same logic of range
    if num_args < 1:
        raise TypeError(f'expected at least 1 argument, got {num_args}')
    elif num_args == 1:
        stop = args[0]
    elif num_args == 2:
        (start, stop) = args
    elif num_args == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expected at most 3 arguments, got {num_args}')

    # generator logic
    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# 5 15 25
