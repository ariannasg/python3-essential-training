#! usr/bin/env python3

words = ['Hello', 'World', '!']
print(f'The words array has {3} elements')

print('Printing elements in words using a while loop:')
n = 0
while n < 3:
    print(words[n])
    n = n + 1

print('Printing elements in words using a for loop:')
for i in words:
    print(i)

print('Trying a while loop using the console input')
secret = 'swordfish'
pw = ''
while pw != secret:
    pw = input("What's the secret word? ")

# CONSOLE OUTPUT:
# The words array has 3 elements
# Printing elements in words using a while loop:
# Hello
# World
# !
# Printing elements in words using a for loop:
# Hello
# World
# !
# Trying a while loop using the console input
# What's the secret word? dunno
# What's the secret word? maybeispwd
# What's the secret word? swordfish
