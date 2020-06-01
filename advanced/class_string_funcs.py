#!usr/bin/env python3


# customize string representations of objects in string and byte forms by
# overriding some class functions
# attention: if the class overrides repr, but not str, then repr will also be
# used to generate the human readable string.
class Person:
    def __init__(self):
        self.fname = 'Ari'
        self.lname = 'Gonzalez'
        self.age = 29

    # use __repr__ to create a string useful for debugging
    def __repr__(self):
        return '<Person Class - fname:{0}, lname:{1}, age:{2}>'.format(
            self.fname, self.lname, self.age)

    # use str for a more human-readable string
    def __str__(self):
        return 'Person ({0} {1}, {2})'.format(
            self.fname, self.lname, self.age)

    # use bytes to convert the informal string to a bytes object
    def __bytes__(self):
        # string to hold the object data
        val = 'Person:{0}:{1}:{2}'.format(self.fname, self.lname, self.age)
        # in order to convert to bytes we need to encode the string
        return bytes(val.encode('utf-8'))


def main():
    # create a new Person object
    cls1 = Person()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print("Formatted: {0}".format(cls1))
    print(bytes(cls1))


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# <Person Class - fname:Ari, lname:Gonzalez, age:29>
# Person (Ari Gonzalez, 29)
# Formatted: Person (Ari Gonzalez, 29)
# b'Person:Ari:Gonzalez:29'
