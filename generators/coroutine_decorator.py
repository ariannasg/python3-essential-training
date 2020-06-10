#!usr/bin/env python3


def coroutine_decorator(func):
    def wrapper_func(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.__next__()
        return cr

    return wrapper_func


@coroutine_decorator
def counter(input_string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item, str):
                if item in input_string:
                    count += 1
                    print(item)
                else:
                    print('No match')
            else:
                print('Not a string')
    except GeneratorExit:
        print(count)


def main():
    # now we can use the coroutine without priming it.
    # It won't throw an error thanks to the decorator
    c = counter('California')
    c.send('Cali')
    c.send('nia')
    c.send(123)
    c.send('HA')
    c.close()


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# Cali
# nia
# Not a string
# No match
# 2
