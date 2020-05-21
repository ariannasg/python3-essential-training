#!usr/bin/env python3


def main():
    print('Reading text files')
    f = open('lines.txt')  # open returns a file object, that's an iterator. by default it opens in read & text mode
    for line in f:
        print(line.rstrip())  # Return a copy of the string with trailing whitespace removed

    print('\nWriting text files')
    infile = open('lines.txt', 'rt')  # open in read mode and text mode
    outfile = open('lines-copy.txt', 'wt')  # open in write mode and text mode
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)  # flushes the output buffer so we ensure we print the "." properly
    outfile.close()  # to prevent any data loss when exiting the main function
    print('\ndone.')

    print('\nWriting binary files')
    infile = open('berlin.jpg', 'rb')  # open in read mode and binary mode
    outfile = open('berlin-copy.jpg', 'wb')   # open in write mode and binary mode
    while True:
        buffer = infile.read(10240)  # 10k bytes
        if buffer:  # is going to be false when is empty
            outfile.write(buffer)
            print('.', end='', flush=True)  # each "." represents 10k bytes read and written
        else:
            break
    outfile.close()
    print('\ndone.')


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT:
# Reading text files
# 01 The first line.
# 02 The second line.
# 03 The third line.
# 04 The fourth line.
# 05 The fifth line.
# 06 The sixth line.
# 07 The seventh line.
# 08 The eight line.
# 09 The ninth line.
# 10 The tenth line.
#
# Writing text files
# ..........
# done.
#
# Writing binary files
# .....................................................
# done.