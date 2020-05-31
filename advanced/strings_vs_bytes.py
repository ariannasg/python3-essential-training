#!usr/bin/env python3


# strings and bytes are not directly interchangeable
# strings contain unicode, while bytes are raw 8-bit values
def main():
    # define some starting values
    # this are bytes correspond to ascii and are encoded in UTF-8
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string"
    print(s)

    # Try combining them. This will cause an error:
    # can only concatenate str (not "bytes") to str
    # print(s+b)

    # Bytes and strings need to be properly encoded and decoded
    # before you can work on them together

    # Decode the bytes using the codec registered for encoding
    s2 = b.decode('utf-8')
    print(s + s2)

    # Encode the string using the codec registered for encoding.
    b2 = s.encode('utf-8')
    print(b + b2)

    # encode the string as UTF-32
    b3 = s.encode('utf-16')
    print(b3)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# b'ABCD'
# This is a string
# This is a stringABCD
# b'ABCDThis is a string'
# b'\xff\xfeT\x00h\x00i\x00s\x00 \x00i\x00s\x00 \x00a\x00 \x00s\x00t\x00r\x00i\x00n\x00g\x00'
