#!usr/bin/env python3


# we can support numerical operations in classes and give objects number-like
# behavior by implementing certain class numerical operation functions
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<Point x:{self.x}, y:{self.y}>'

    # implement addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # implement subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # implement in-place addition
    # Python supports in-place math operations on objects. These functions are
    # called when you use the short-hand notation such as plus equals in order
    # to add to an existing object in place. This means I'm modifying the
    # object rather than creating a new one.
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


def main():
    print('Declare some points')
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1)
    print(p2)

    print('Add two points')
    # if the addition is not defined, when trying to sum points I'll get
    # TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
    p3 = p1 + p2
    print(p3)

    print('subtract two points')
    p4 = p2 - p1
    print(p4)

    print('Perform in-place addition')
    p1 += p2
    print(p1)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# Declare some points
# <Point x:10, y:20>
# <Point x:30, y:30>
# Add two points
# <Point x:40, y:50>
# subtract two points
# <Point x:20, y:10>
# Perform in-place addition
# <Point x:40, y:50>
