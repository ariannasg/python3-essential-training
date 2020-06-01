#!usr/bin/env python3
import os
import secrets

# the secrets module was introduced in Python 3.6 for using
# cryptographic-appropriate methods to generate random data that may be
# sensitive.

# the urandom() function in the OS module produces random numbers that
# are cryptographically safe to use for sensitive purposes.
# it's unlikely we'll use this function directly
# using 8 bytes
result = os.urandom(8)
print(result)
print([hex(b) for b in result])

# secrets.choice is the same as random.choice but more secure
moves = ["rock", "paper", "scissors"]
print(secrets.choice(moves))

# secrets.token_bytes generates random bytes
result = secrets.token_bytes(8)
print(result)

# secrets.token_hex creates a random string in hexadecimal
result = secrets.token_hex(8)
print(result)

# secrets.token_urlsafe generates characters that can be in URLs
result = secrets.token_urlsafe(8)
print(result)

# CONSOLE OUTPUT (it will vary!):
# b'\xd7\xec\xa6\xde\x83\x8f\xd5\x1d'
# ['0xd7', '0xec', '0xa6', '0xde', '0x83', '0x8f', '0xd5', '0x1d']
# rock
# b'\xf0\x80\x15\xa8\xa0b\x1a5'
# 160e82087efc5241
# k1ZIFAVjvlE
