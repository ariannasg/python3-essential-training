#!usr/bin/env python3
from generators.coroutine_decorator import coroutine_decorator


# Coroutines are used to consume values, but they need a producer that will
# send it values to consume.
# The initial producer is not going to be a coroutine.
@coroutine_decorator
def match_counter(string):
    count = 0
    try:
        while True:
            line = yield
            if string in line:
                count += 1
    except GeneratorExit:
        print(f'{string}: {count}')


@coroutine_decorator
def longer_than(n):
    count = 0
    try:
        while True:
            line = yield
            if len(line) > n:
                print(line)
                count += 1
    except GeneratorExit:
        print(f'longer than {n}: {count}')


# this is the producer
def sender(filename, target_coroutine):
    for line in open(filename):
        target_coroutine.send(line)
    target_coroutine.close()


def main():
    sender('names.txt', match_counter('Dal'))
    sender('names.txt', longer_than(20))


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# Dal: 1
# Brittanie Talamantes
#
# longer than 20: 1
