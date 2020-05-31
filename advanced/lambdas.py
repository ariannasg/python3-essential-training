#!usr/bin/env python3


# lambdas are simple and small anonymous functions that are used in situations
# where defining a whole separate function would unnecessarily increase the
# complexity of the code and reduce readability.
# Lambdas can be used as in-place functions when using built-ins conversion
# functions like filter, map, etc
def celsius_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9


def main():
    celsius_temps = (0, 12, 34, 100)
    fahrenheit_temps = (32, 65, 100, 212)

    # Use regular functions to convert temps
    print(list(map(fahrenheit_to_celsius, fahrenheit_temps)))
    print(list(map(celsius_to_fahrenheit, celsius_temps)))

    # Use lambdas to accomplish the same thing
    # reducing the complexity of the code
    print(list(map(lambda temp: (temp - 32) * 5 / 9, fahrenheit_temps)))
    print(list(map(lambda temp: (temp * 9 / 5) + 32, celsius_temps)))

    # using lambda as the filter function
    odd_f_temps = list(filter(lambda temp: (temp % 2) != 0, fahrenheit_temps))
    print(odd_f_temps)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# [0.0, 18.333333333333332, 37.77777777777778, 100.0]
# [32.0, 53.6, 93.2, 212.0]
# [0.0, 18.333333333333332, 37.77777777777778, 100.0]
# [32.0, 53.6, 93.2, 212.0]
# [65]
