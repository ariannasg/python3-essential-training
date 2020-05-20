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
