#!/usr/bin/env python3


class InclusiveRange:
    def __init__(self, *args):
        num_args = len(args)
        self._start = 0
        self._step = 1
        
        if num_args < 1:
            raise TypeError(f'expected at least 1 argument, got {num_args}')
        elif num_args == 1:
            self._stop = args[0]
        elif num_args == 2:
            (self._start, self._stop) = args
        elif num_args == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError(f'expected at most 3 arguments, got {num_args}')

        self._next = self._start
    
    def __iter__(self):  # identifies this object as an iterator object
        return self

    def __next__(self):  # identifies the loop logic
        if self._next > self._stop:
            raise StopIteration
        else:
            _value = self._next
            self._next += self._step
            return _value


def main():
    for n in InclusiveRange(25):
        print(n, end=' ')
    print()
    for n in InclusiveRange(5, 25):
        print(n, end=' ')
    print()
    for n in InclusiveRange(5, 25, 10):
        print(n, end=' ')
    print()


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# 5 15 25