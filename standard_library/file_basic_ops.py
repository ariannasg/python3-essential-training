#!usr/bin/env python3

# when I create a context manager, I don't have to worry about closing the file
# when I'm done with it; the context manager will simply do it for me.
# for creating a context manager we simple use "with" before "open"

# open a file for writing data
# "w" means write, "r" means read, "a" means append,
# i.e: "r+" means read and write, "a+" means append read and write
fp = open("testfile.txt", "w")
fp.write("This is some text data\n")
fp.close()

# read a file's data using a context manager
with open("testfile.txt", "r") as fp:
    data = fp.read()
    print(data)

# Add data to an existing file
with open("testfile.txt", "a+") as fp:
    fp.write("This is data added to the file\n")
    # I set the position at 0, back at the beginning of the file for reading
    fp.seek(0)
    data = fp.read()
    print(data)

# CONSOLE OUTPUT:
# This is some text data
#
# This is some text data
# This is data added to the file
