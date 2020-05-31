#!usr/bin/env python3
import time


# Decorators are special type of function that returns a wrapper function.
# In python everything is an object! function is a type of object.
def main():
    x = func1
    x()
    big_sum()


def func1():
    print('this is func1')

    def func2():
        print('this is func2')

    return func2()


def func3():
    print('this is func3')


def elapsed_time(f):
    def wrapper():
        print(f'Inside decorator function')
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')

    return wrapper


@elapsed_time
def big_sum():
    num_list = []
    for num in (range(25)):
        print(num, end=' ')
        num_list.append(num)
    print(f'\nBig sum: {sum(num_list)}')


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# this is func1
# this is func2
# Inside decorator function
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
# Big sum: 300
# Elapsed time: 0.14400482177734375 ms
