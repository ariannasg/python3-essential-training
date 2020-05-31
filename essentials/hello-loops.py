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
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt:
        break
    if count == 3:
        continue
    pw = input(f"{count}: What's the secret word? ")
else:
    auth = True

print('Authorised' if auth else 'Calling the FBI ...')

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
# 1: What's the secret word? x
# 2: What's the secret word? y
# 4: What's the secret word? a
# 5: What's the secret word? x
# Calling the FBI ...

# Trying a while loop using the console input
# 1: What's the secret word? x
# 2: What's the secret word?
# 4: What's the secret word? a
# 5: What's the secret word? swordfish
# Authorised
