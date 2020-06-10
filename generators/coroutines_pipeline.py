#!usr/bin/env python3
from generators.coroutine_decorator import coroutine_decorator


# It is possible for a single coroutine to both send and receive values.
# Similar to the pipelines we create with generators, coroutines can also be
# used to create data pipelines.
@coroutine_decorator
def router():
    try:
        while True:
            line = yield
            (first, last) = line.split(' ')
            fnames.send(first)
            lnames.send(last.rstrip())
    except GeneratorExit:
        fnames.close()
        lnames.close()


@coroutine_decorator
def file_write(filename):
    try:
        with open(filename, 'w') as file:
            while True:
                line = yield
                file.write(line + '\n')
    except GeneratorExit:
        file.close()
        print('one file created')


if __name__ == '__main__':
    fnames = file_write('first_names.txt')
    lnames = file_write('last_names.txt')
    router = router()
    for name in open('names.txt'):
        router.send(name)
    router.close()

# CONSOLE OUTPUT:
# one file created
# one file created
