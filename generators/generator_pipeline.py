#!usr/bin/env python3


def separate_names(names):
    for full_name in names:
        for name in full_name.split(' '):
            yield name


def get_longest_name(file):
    full_names = (name.strip() for name in open(file))
    names = separate_names(full_names)
    lengths = ((name, len(name)) for name in names)

    return max(lengths, key=lambda x: x[1])


def main():
    print(get_longest_name('names.txt'))


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# ('Humbertson', 10)
