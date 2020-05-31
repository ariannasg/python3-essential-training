#!usr/bin/env python3
import itertools


# itertools is a module that's not technically a set of built-in functions but
# it is part of the standard library that comes with python.
# it's useful for for creating and using iterators.
def main():
    print('some infinite iterators')
    # cycle iterator can be used to cycle over a collection over and over
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # use count to create a simple counter
    count1 = itertools.count(100, 3)
    print(next(count1))
    print(next(count1))
    print(next(count1))

    print('some non-infinite iterators')
    values = [10, 5, 20, 30, 40, 50, 40, 30]

    # accumulate creates an iterator that accumulates/aggregates values
    print(list(itertools.accumulate(values)))  # this defaults to addition
    print(list(itertools.accumulate(values, max)))
    print(list(itertools.accumulate(values, min)))

    # use chain to connect sequences together
    x = itertools.chain('ABCD', '1234')
    print(list(x))

    # dropwhile and takewhile will return values until
    # a certain condition is met that stops them. they are similar to the
    # filter built-in function.
    # dropwhile will drop the values from the sequence as long as the
    # condition of the function is true and then returns the rest of values
    print(list(itertools.dropwhile(is_less_than_forty, values)))
    # takewhile will keep the values from the sequence as long as the
    # condition of the function is true and then stops giving data
    print(list(itertools.takewhile(is_less_than_forty, values)))


def is_less_than_forty(x):
    return x < 40


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# some infinite iterators
# Joe
# John
# Mike
# Joe
# John
# 100
# 103
# 106
# some non-infinite iterators
# [10, 15, 35, 65, 105, 155, 195, 225]
# [10, 10, 20, 30, 40, 50, 50, 50]
# [10, 5, 5, 5, 5, 5, 5, 5]
# ['A', 'B', 'C', 'D', '1', '2', '3', '4']
# [40, 50, 40, 30]
# [10, 5, 20, 30]
