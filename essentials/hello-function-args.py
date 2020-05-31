#! usr/bin/env python3

# Function arguments in python work in the same way as assignments - be careful with mutable objects


# When assigning a mutable to a var, we are actually assigning a reference to the mutable
# Function arguments work in the same way as assignments. Changes to mutable objects will be reflected on the caller
# Immutable objects won't change so changes to the object won't be reflected on the caller
def main():
    a = [5]
    print(id(a))
    b = a
    print(id(b))
    b[0] = 3
    print(id(b))

    x = 5
    print(id(x))
    y = x
    print(id(y))
    kitten(x)
    print(f'in main: x is {x}')
    dog('wofwof', 'woooof', 'woffff')
    dog()
    n = ('wofwof', 'woooof', 'woffff')
    dog(n)
    dog(*n)
    cow(Buffy='muuu', Zilla='mmm', Angel='mumu')
    cow()
    m = dict(Buffy='muuu', Zilla='mmm', Angel='mumu')
    cow(**m)


def kitten(a):
    print(id(a))
    a = 3
    print(id(a))
    print('Meow.')
    print(a)


def dog(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Woof.')


def cow(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Cow {} says {}'.format(k, kwargs[k]))
    else:
        print('Mu.')


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# 4328377664
# 4328377664
# 4328377664
# 4323715872
# 4323715872
# 4323715872
# 4323715808
# Meow.
# 3
# in main: x is 5
# wofwof
# woooof
# woffff
# Woof.
# ('wofwof', 'woooof', 'woffff')
# wofwof
# woooof
# woffff
# Cow Buffy says muuu
# Cow Zilla says mmm
# Cow Angel says mumu
# Mu.
# Cow Buffy says muuu
# Cow Zilla says mmm
# Cow Angel says mumu
