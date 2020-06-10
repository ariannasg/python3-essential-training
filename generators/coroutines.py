#!usr/bin/env python3


# While technically a coroutine object is a generator object, they are
# different concepts. A coroutine is designed to repeatedly send input to it,
# process that input by following the logical path that you program it to
# follow, and stop when it reaches the yield statement.
# Unlike generators, coroutines are not for iterating over sequences.
# A coroutine is an object that supports the send() method in order to
# receive and process input and maintain internal state.
# We need to "prime" a coroutine by calling next on it or by sending a None
# value to it after it's instantiated. A good solution to this problem is using
# the coroutine decorator
def coroutine_counter_example(input_string):
    count = 0
    try:
        while True:
            item = yield   # this is the input passed via the "send()" method
            if isinstance(item, str):
                if item in input_string:
                    count += 1
                    print(item)
                else:
                    print('No match')
            else:
                print('Not a string')
    # It is good practice use a GeneratorExit block. This is so that when
    # we're done with the coroutine, we can close it out, which will raise
    # the GeneratorExit exception. By handling the exception, I can also
    # provide some action that I want to occur upon closing the coroutine.
    except GeneratorExit:
        print(count)


def main():
    # if I don't start by doing next() I'll get:
    # TypeError: can't send non-None value to a just-started generator
    c = coroutine_counter_example('California')
    c.__next__()
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
