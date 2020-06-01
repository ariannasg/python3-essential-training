#!/usr/bin/env python3
from math import pi


# Comprehension is a technique for creating sequences based in another sequence
# Comprehensions can be applied to lists, sets, and dictionaries.
def main():
    seq = range(11)
    print_list(seq)
    seq2 = [x * 2 for x in seq]
    print_list(seq2)
    seq3 = [x for x in seq if x % 2 == 0]  # elements that are divisible by 2
    print_list(seq3)
    seq4 = [(x, x**2) for x in seq]  # create tuples of elements in seq and its squared
    print_list(seq4)
    seq4 = [round(pi, x) for x in seq]  # pi rounded to the number of decimals according to our seq
    print_list(seq4)
    seq5 = {x: x**2 for x in seq}  # create a dict with each element in seq as key and its squared as val
    print(seq5)
    seq5 = {x: x ** 2 for x in seq}  # create a dict with each element in seq as key and its squared as val
    print(seq5)
    seq6 = set(x for x in 'superduper' if x not in 'pd')  # create a set with letters in 'superduper' except p and d
    print(seq6)


def print_list(o):
    for x in o:
        print(x, end=' ')
    print()


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# 0 1 2 3 4 5 6 7 8 9 10
# 0 2 4 6 8 10 12 14 16 18 20
# 0 2 4 6 8 10
# (0, 0) (1, 1) (2, 4) (3, 9) (4, 16) (5, 25) (6, 36) (7, 49) (8, 64) (9, 81) (10, 100)
# 3.0 3.1 3.14 3.142 3.1416 3.14159 3.141593 3.1415927 3.14159265 3.141592654 3.1415926536
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# {'u', 'e', 's', 'r'}
