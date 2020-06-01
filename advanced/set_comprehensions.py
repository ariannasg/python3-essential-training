#!usr/bin/env python3


def main():
    # define a list of temperature data points
    c_temps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]
    print(c_temps)

    # build a list of Fahrenheit temperatures
    f_temps1 = [(t * 9 / 5) + 32 for t in c_temps]
    print(f_temps1)

    # build a set of unique Fahrenheit temperatures
    f_temps2 = {(t * 9 / 5) + 32 for t in c_temps}
    print(f_temps2)

    # build a set from an input source using a set comprehension and a
    # predicate condition
    temp_str = "The quick brown fox jumped over the lazy dog"
    chars = {c.upper() for c in temp_str if not c.isspace()}
    print(chars)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT (the 2 set outputs will vary):
# [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]
# [41.0, 50.0, 53.6, 57.2, 50.0, 73.4, 105.8, 86.0, 53.6, 75.2, 53.6, 64.4, 84.2]
# {64.4, 73.4, 41.0, 105.8, 75.2, 50.0, 84.2, 53.6, 86.0, 57.2}
# {'A', 'F', 'R', 'I', 'B', 'L', 'V', 'D', 'X', 'O', 'G', 'W', 'Z', 'U', 'T', 'C', 'P', 'K', 'Q', 'J', 'E', 'H', 'M', 'N', 'Y'}
