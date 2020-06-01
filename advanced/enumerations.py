#!usr/bin/env python3
from enum import Enum, unique, auto


# we can define enumerations by using the Enum class as a super class.
# are used to assign easy-to-read names to constant values in a program,
# which increases the readability of your code. they can also be used as hash
# values, and we can iterate over them like we would other iterables.
# we can't have duplicate names in enums.
# we can have duplicate values in enums unless we enforce unique values using
# the @unique decorator.
@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    # TOMATO = 5 -> TypeError: Attempted to reuse key: 'TOMATO'
    # APRICOT = 4
    # v ValueError: duplicate values found in <enum 'Fruit'>: APRICOT -> TOMATO
    PEAR = auto()


def main():
    # enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(str(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # enums have name and value properties
    print(Fruit.APPLE.name)
    print(Fruit.APPLE.value)

    # print the auto-generated value
    print(Fruit.PEAR.name)
    print(Fruit.PEAR.value)

    # enums are hashable - can be used as keys
    my_fruits = {Fruit.BANANA: "Come Mr. Tally-man"}
    print(my_fruits[Fruit.BANANA])


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# Fruit.APPLE
# <enum 'Fruit'>
# Fruit.APPLE
# <Fruit.APPLE: 1>
# APPLE
# 1
# PEAR
# 5
# Come Mr. Tally-man
