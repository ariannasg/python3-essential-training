#!usr/bin/env python3


#  It's important to note the distinction between a generator object and a
#  generator function. The generator function returns a generator object 
#  and that generator object will yield the values.
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


def main():
    print(type(even_integers_generator(8)))
    print(list(even_integers_generator(8)))


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# <class 'generator'>
# [0, 2, 4, 6]
