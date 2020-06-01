#!usr/bin/env python3
import string
from collections import deque


# a deque it's sort of a hybrid object between a stack and a queue, the name
# means double-ended queue. we can append or pop data from either side; they
# are designed to be memory-efficient when accessing them from either end.
# Deques can be initialized to be either empty or get their initial data from
# an existing, iterable object, and they can also be specified to have a max
# length. To add data to a deque, we use either the append or append left
# methods. similarly, items can be removed using either pop or pop left.
# Deques also support a rotate function, which can operate in either direction.
# The rotate function takes a parameter indicating how many items to rotate
# (with default = 1), so positive numbers will rotate to the right,
# while negative numbers will rotate to the left.
# use a deqye if you have a use case where you need to be able to operate on
# both ends of a list and perform operations such as this rotation,
# i.e: a restaurant sign-up list might have such a need
def main():
    # initialize a deque with lowercase letters
    d = deque(string.ascii_lowercase)

    # deques support the len() function
    print("Item count:", len(d))

    # deques can be iterated over
    for elem in d:
        print(elem, end=" ")

    print()
    print('initial:', d)

    # manipulate items from either end
    d.pop()
    print('after poping:', d)

    d.popleft()
    print('after poping left:', d)

    d.append(2)
    d.appendleft(1)
    print('after appending 2 and appending 1 to the left:', d)

    # rotate the deque
    d.rotate(1)
    print('after rotating 1:', d)
    d.rotate(3)
    print('after rotating 3:', d)
    d.rotate(-3)
    print('after rotating -3:', d)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# Item count: 26
# a b c d e f g h i j k l m n o p q r s t u v w x y z
# initial: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
# after poping: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'])
# after poping left: deque(['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'])
# after appending 2 and appending 1 to the left: deque([1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 2])
# after rotating 1: deque([2, 1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'])
# after rotating 3: deque(['w', 'x', 'y', 2, 1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'])
# after rotating -3: deque([2, 1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'])
