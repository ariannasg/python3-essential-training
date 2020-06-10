#!usr/bin/env python3


# Create a generator object that will yield the Fibonacci sequence.
# 1 1 2 3 5 8 13 21 34 55
def fibonacci():
    # we need to always keep the state of the previous 2 nums in the seq
    previous_number, number = 0, 1
    while True:
        yield number
        previous_number, number = number, previous_number + number


def main():
    fib = fibonacci()
    print('The first 10 nums of the fibonacci seq:')
    for _ in range(10):
        print(fib.__next__())


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# The first 10 nums of the fibonacci seq:
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
