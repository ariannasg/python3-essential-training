#! usr/bin/env python3


def function(n=1):
    print(n)


function()  # prints 1
function(42)  # prints 42
# In python there is no difference between a function and a procedure, all functions return values
print(function())  # prints None
print('---\t')


def function2(n=1):
    print(n)
    return n * 2


function2()  # prints 1
function2(42)  # prints 42
print(function2())  # prints 2
print('---\t')


def is_prime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


def list_primes():
    print('Prime numbers from 0 to 99: ', end=' ')
    for n in range(100):
        if is_prime(n):
            print(n, end=' ', flush=True)


list_primes()

# CONSOLE OUTPUT:
# 1
# 42
# 1
# None
# ---
# 1
# 42
# 1
# 2
# ---
# Prime numbers from 0 to 99:  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
