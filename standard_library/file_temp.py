#!usr/bin/env python3
import os
import tempfile

# The tempfile module gives us functions for working with temporary data,
# and also allows us to examine properties related to these files.
# we can create temp files and operate with them using either the mkstemp
# function or the TemporaryFile and TemporaryDirectory classes
# using the TemporaryFile and TemporaryDirectory classes is more "pythonic"

# we can use the gettempdir and gettempprefix functions to see which directory
# files will be saved to, and what file prefix they'll be given.
# get information about the temp data environment
print('gettempdir():', tempfile.gettempdir())
print('gettempprefix():', tempfile.gettempprefix())

# create a temporary file using mkstemp().
# attention! mkstemp does not automatically delete the file for me!
# The of mkstemp is a tuple (fd, name) where fd is the file descriptor
# returned by os.open, and name is the filename.
(temp_file_handler, temp_file_pointer) = tempfile.mkstemp(".tmp", "testTemp",
                                                          None, True)
f = os.fdopen(temp_file_handler, "w+t")
f.write('This is some text data')
f.seek(0)
print(f.read())
f.close()
os.remove(temp_file_pointer)

# create a temp file using the TemporaryFile class
# here we're using the context manager syntax, so we don't need to worry about
# closing and removing the file
with tempfile.TemporaryFile(mode="w+t") as temp_file_pointer2:
    temp_file_pointer2.write('This is some more text data')
    temp_file_pointer2.seek(0)
    print(temp_file_pointer2.read())

# create a temporary directory using the TemporaryDirectory class
with tempfile.TemporaryDirectory() as temp_dir_pointer:
    path = os.path.join(temp_dir_pointer, "tempfile.txt")
    temp_file_pointer3 = open(path, "w+t")
    temp_file_pointer3.write("This is a temp file in temp dir")
    temp_file_pointer3.seek(0)
    print(temp_file_pointer3.read())

# CONSOLE OUTPUT:
# gettempdir(): /var/folders/x5/7_2_6w4d70d12t74wnr_3vz40000gn/T
# gettempprefix(): tmp
# This is some text data
# This is some more text data
# This is a temp file in temp dir
