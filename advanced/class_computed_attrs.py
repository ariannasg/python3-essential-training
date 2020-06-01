#!usr/bin/env python3


# classes can use methods to control how attributes are accessed on an object.
# Whenever an object's attributes are retrieved or set, Python calls one of
# these functions to give your class an opportunity to perform any desired
# processing.
# getattribute and getattr, are called to retrieve an attribute value.
# getattr is called only when the requested attribute can't be found on the
# object.
# getattribute is called every time an attribute name is requested and when
# Python goes to look up any methods on your class.
# setattr is called when an attribute value is set on the object.
# delattr is called to delete an attribute.
# dir is called when the dir function is used on the object.
class Color:
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == 'rgbcolor':
            return self.red, self.green, self.blue
        elif attr == 'hexcolor':  # format the values to 2 char hex strings
            return '#{0:02x}{1:02x}{2:02x}'.format(
                self.red, self.green, self.blue)
        else:
            raise AttributeError

    # use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == 'rgbcolor':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            # always make sure you call the super class.
            # reason: in the constructor I've got some existing attributes.
            # when the class is initialized and the assignment statements
            # are executed, the __setattr__ is going to be called for each
            # attribute. if you don't call the super.setattr, then the
            # __getattr__ function will be called instead. And since it's not
            # one of the attr we have defined, an attribute error will be
            # raised.
            super().__setattr__(attr, val)

    # use dir to list the available properties
    def __dir__(self):
        return 'rgbolor', 'hexcolor'


def main():
    # create an instance of Color
    cls1 = Color()
    # print the value of a computed attribute
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # set the value of a computed attribute
    cls1.rgbcolor = (125, 200, 86)
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # access a regular attribute
    print(cls1.red)

    # list the available properties
    print(dir(cls1))

    # list the available properties of the str class
    print(dir(str))


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# (50, 75, 100)
# #324b64
# (125, 200, 86)
# #7dc856
# 125
# ['hexcolor', 'rgbolor']
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
