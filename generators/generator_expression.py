#!usr/bin/env python3


# list comprehension: [item.upper() for item in ['a', 'b']]
# generator expression which evaluates to a generator object:
# (item.upper() for item in ['a', 'b'])

# This is what we get in the console if we operate with the next method:
# x =(item.upper() for item in ['a', 'b'])
# x.__next__()
# 'A'
# x.__next__()
# 'B'
# x.__next__()
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration

names_list = ['Adam', 'Anne', 'Barry', 'Brianne', 'Charlie', 'Cassandra',
              'David', 'Dana']

uppercase_names = (name.upper() for name in names_list)
reverse_uppercase = (name[::-1] for name in list(uppercase_names))


def main():
    print(names_list)
    print(uppercase_names)
    print(list(uppercase_names))
    print(reverse_uppercase)
    print(list(reverse_uppercase))


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT: (Attention at why the empty [])!
# ['Adam', 'Anne', 'Barry', 'Brianne', 'Charlie', 'Cassandra', 'David', 'Dana']
# <generator object <genexpr> at 0x1057b3580>
# []
# <generator object <genexpr> at 0x1057437b0>
# ['MADA', 'ENNA', 'YRRAB', 'ENNAIRB', 'EILRAHC', 'ARDNASSAC', 'DIVAD', 'ANAD']
