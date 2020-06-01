#!usr/bin/env python3


# We use list comprehension to derive a new list of values from an
# existing list of values while keeping the code as simple and readable as
# possible.
# we can use predicate conditions on the comprehension for filtering results.
def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # Perform a mapping and filter function on a list
    filtered_even_squared = list(
        map(lambda e: e ** 2, filter(lambda e: 4 < e < 16, evens)))
    print(filtered_even_squared)

    # Derive a new list of numbers from a given list
    even_squared = [e ** 2 for e in evens]
    print(even_squared)

    # Limit the items operated on with a predicate condition
    filtered_odd_squared = [e ** 2 for e in odds if 3 < e < 17]
    print(filtered_odd_squared)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# [36, 64, 100, 144, 196]
# [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
# [25, 49, 81, 121, 169, 225]
