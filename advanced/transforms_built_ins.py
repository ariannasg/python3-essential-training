#!usr/bin/env python3


# built-in function to transform sequences of data, i.e: sorted, filter, map
def filter_func(x):
    # if number is even then the number should be excluded from the result
    if x % 2 == 0:
        return False
    return True


def filter_func_2(x):
    # if char is upper case then it should be excluded from the result
    if x.isupper():
        return False
    return True


def square_func(x):
    return x ** 2


def to_grade(x):
    if x >= 90:
        return 'A'
    elif 80 <= x < 90:
        return 'B'
    elif 70 <= x < 80:
        return 'C'
    elif 65 <= x < 70:
        return 'D'
    return 'F'


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = 'abcDeFGHiJklmnoP'
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # use filter to remove items from a list
    print(filter(filter_func, nums))
    odds = list(filter(filter_func, nums))
    print(odds)

    # use filter on non-numeric sequence
    lowers = list(filter(filter_func_2, chars))
    print(lowers)

    # use map to create a new sequence of values
    print(map(square_func, nums))
    squares = list(map(square_func, nums))
    print(squares)

    # use sorted and map to change numbers to grades
    grades = sorted(grades)
    letters = list(map(to_grade, grades))
    print(letters)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# <filter object at 0x10958fa00>
# [1, 5, 13, 381, 47]
# ['a', 'b', 'c', 'e', 'i', 'k', 'l', 'm', 'n', 'o']
# <map object at 0x108916ee0>
# [1, 64, 16, 25, 169, 676, 145161, 168100, 3364, 2209]
# ['F', 'D', 'C', 'C', 'B', 'B', 'A', 'A']
