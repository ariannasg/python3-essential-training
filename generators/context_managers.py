#!usr/bin/env python3
from contextlib import contextmanager


# A context manager is a Python object that is able to act as a control
# structure when used after the "with" statement.
# Analogy: people that sort out travelling rock bands by setting up the stage,
# letting them play and then tearing down everything, packing instruments, etc.
#  Not all Python objects can act as a context manager. For a Python object to
#  be able to act as a context manager, it must implement the methods
#  "enter" and "exit." For example an open file object do implement these.
# There are 3 steps that a context manager takes: Setting up a context,
# giving control back to the caller, and wrapping up once the color is done.
# We can achieve these steps by also using a generator to produce a context
# manager. The steps are accomplished with three key words, "try", "yield" and
# "finally."
# Context managers allow easy execution of setup code and wrap-up code with
# the help of Python generators and the context manager decorator.

@contextmanager
def simple_context_manager(obj):
    """ Increments some_property by 1.
     It returns a generator object that acts as a context manager thanks to
    the decorator
    """
    try:  # setup statement
        obj.some_property += 1
        # yield causes this context manager to pause and yield control
        # back to the caller to do a particular action or actions
        yield
    finally:  # wrap up statement
        obj.some_property -= 1


class SomeObj:
    def __init__(self, value):
        self.some_property = value


def main():
    obj = SomeObj(5)
    print(obj.some_property)

    with simple_context_manager(obj):
        print(obj.some_property)

    print(obj.some_property)


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# 5
# 6
# 5
