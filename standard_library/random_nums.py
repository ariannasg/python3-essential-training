#!usr/bin/env python3
import random

# a PRNG (pseudo-random number generator) work by using a random value as a
# seed value, usually based on the system time or some other random value,
# and then they use that number to derive a random value.
# a CSPRNG (cryptographically secure random number generators) are suitable for
# sensitive-use cases like ciphers or passwords. these values are usually
# generated in a platform specific way depending on the operating system that
# the Python Program is running on.

# create a random number - by default random() returns a value between 0 and 1
print(random.random())
print(random.random())
print(random.random())

# implement a coin toss function
print()
for i in range(4):
    if random.random() <= 0.5:
        print("Heads")
    else:
        print("Tails")

# get a random number within a range
print()
print(random.uniform(1, 100))
print(random.uniform(1, 100))

# generate random integers within a given range
print()
print(random.randint(1, 100))
print(random.randint(1, 100))

# generate random integers with a step function
# this example chooses from 0 to 100 stepped by 5
print()
print(random.randrange(0, 101, 5))
print(random.randrange(0, 101, 5))

# Use the seed function to position the generator so we can reproduce the
# random values and obtain predictable results.
# these results will always be the same.
# this is one of the reasons why normal random numbers are not secure enough
# for sensitive data usage
print()
random.seed(1)
print(random.random())
print(random.random())
print("----------------")
random.seed(1)
print(random.random())
print(random.random())

# CONSOLE OUTPUT (it will vary except the last 4 results!):
# 0.3503433852051838
# 0.9670902208101603
# 0.9167049464225621
#
# Heads
# Tails
# Heads
# Tails
#
# 75.23146498274643
# 32.02874760965268
#
# 59
# 26
#
# 100
# 25
#
# 0.13436424411240122
# 0.8474337369372327
# ----------------
# 0.13436424411240122
# 0.8474337369372327