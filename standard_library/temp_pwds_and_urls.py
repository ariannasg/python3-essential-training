#!usr/bin/env python3
import secrets
import string
# Create a temporary password and URL using Python


# Function to return a temporary password given a length
def generate_temp_pass(num_chars=8):
    potential_chars = string.ascii_letters + string.digits + "+=?/!@#$%*"
    return ''.join(secrets.choice(potential_chars) for i in range(num_chars))


# Function to return a temporary password and enforce 1 number and 1 uppercase
def generate_better_pass(num_chars=8):
    potential_chars = string.ascii_letters + string.digits + "+=?/!@#$%*"
    while True:
        result = ''.join(
            secrets.choice(potential_chars) for i in range(num_chars))
        # stop if the password has at least one number and one uppercase char
        if (any(c.isupper() for c in result) and
                any(c.isdigit() for c in result)):
            break

    return result


# create a temporary password
print(generate_temp_pass(10))
# create a stronger temporary password
print(generate_better_pass(10))

# create a temporary, hard-to-guess URL for example for account verification
resultUrl = "https://my.example.com?reset="
resultUrl += secrets.token_urlsafe(15)
print(resultUrl)

# CONSOLE OUTPUT (it will vary!):
# srnm1IY/+s
# gsOzYWii5i
# https://my.example.com?reset=D_uRRr1RedR7kjJKfg02
