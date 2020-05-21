#!usr/bin/env python3

import random as r
import datetime as d


def main():
    x = list(range(26))
    print(x)
    r.shuffle(x)
    print(x)  # it will print a shuffled x every time

    now = d.datetime.now()
    print(now)
    print(now.year, now.month)


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# [14, 18, 23, 22, 21, 25, 7, 0, 9, 19, 11, 20, 13, 24, 5, 10, 17, 15, 3, 4, 1, 6, 8, 2, 12, 16]
# 2020-05-21 15:14:57.295696
# 2020 5
