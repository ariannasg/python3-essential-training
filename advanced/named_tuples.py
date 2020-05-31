#!usr/bin/env python3
import collections


# the collections module defines more advanced collections data structures.
# namedtuples is an example of these. namedtuples can help make the code more
# readable when what we need is a lightweight immutable class.
# they do have limitations, such as they can't use default argument values
# and such, so if the data that we're working with has a large number of
# optional properties it might be better to just go with a regular class.
# the point example is a perfect example of when to use them, since it's much
# simpler and readable to use namedtuples than to create a Point class
def main():
    # create a Point namedtuple
    point = collections.namedtuple('Point', 'x y')

    p1 = point(10, 20)
    p2 = point(30, 40)

    print(type(p1))
    print(isinstance(p1, point))

    print(p1, p2)
    print(p1.x, p1.y)

    # the replace function allows to create a new instance of the namedtuple
    # while replacing specified fields with a new value.
    p1 = p1._replace(x=100)
    print(p1)
    p1 = p1._replace(x=30, y=55)
    print(p1)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# <class '__main__.Point'>
# True
# Point(x=10, y=20) Point(x=30, y=40)
# 10 20
# Point(x=100, y=20)
# Point(x=30, y=55)
