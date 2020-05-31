#!usr/bin/env python3
from decimal import Decimal


# in python any object is considered to be True unless its class defines a
# bool method that returns false or has a len method returning 0
def main():
    print(bool(False))
    print(bool(0))
    print(bool(0.0))
    print(bool(0j))
    print(bool(Decimal(0)))
    print(bool([]))
    print(bool({}))
    print(bool(set()))
    print(bool(range(0)))


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
