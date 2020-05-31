#!/usr/bin/env python3

x = 0x0a
y = 0x0f

print('Bitwise and operator')
z = x & y
print(f'(hexadecimal) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(binary) x is {x:08b}, y is {y:08b}, z is {z:08b}')

print('Bitwise or operator')
z = x | y
print(f'(hexadecimal) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(binary) x is {x:08b}, y is {y:08b}, z is {z:08b}')

print('Bitwise exclusive or operator')
z = x ^ y
print(f'(hexadecimal) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(binary) x is {x:08b}, y is {y:08b}, z is {z:08b}')

print('Bitwise shift left operator')
z = x << y
print(f'(hexadecimal) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(binary) x is {x:08b}, y is {y:08b}, z is {z:08b}')

print('Bitwise shift right operator')
z = x >> y
print(f'(hexadecimal) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(binary) x is {x:08b}, y is {y:08b}, z is {z:08b}')

# CONSOLE OUTPUT:
# Bitwise and operator
# (hexadecimal) x is 0a, y is 0f, z is 0a
# (binary) x is 00001010, y is 00001111, z is 00001010
# Bitwise or operator
# (hexadecimal) x is 0a, y is 0f, z is 0f
# (binary) x is 00001010, y is 00001111, z is 00001111
# Bitwise exclusive or operator
# (hexadecimal) x is 0a, y is 0f, z is 05
# (binary) x is 00001010, y is 00001111, z is 00000101
# Bitwise shift left operator
# (hexadecimal) x is 0a, y is 0f, z is 50000
# (binary) x is 00001010, y is 00001111, z is 1010000000000000000
# Bitwise shift right operator
# (hexadecimal) x is 0a, y is 0f, z is 00
# (binary) x is 00001010, y is 00001111, z is 00000000
