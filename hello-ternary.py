#!usr/bin/env python3

# Ternary conditional operator exists since python 2.6
hungry = True
x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
print(x)

hungry = None
x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
print(x)

# CONSOLE OUTPUT:
# Feed the bear now!
