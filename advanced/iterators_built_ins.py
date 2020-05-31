#!usr/bin/env python3


def main():
    # define a list of days in English and French
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    days_spanish = ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab']

    # use iter to create an iterator over a collection
    i = iter(days)
    print(next(i))  # Sun
    print(next(i))  # Mon
    print(next(i))  # Tue

    # iterate using a function and a sentinel
    with open('testfile.txt', 'r') as fp:
        # the readline function retrieves the next line I'm going to read.
        # '' is the sentinel value.
        # when the value that is being returned by the readline function is
        # equal to the sentinel value, the iterator will stop.
        # in this case the iterator is looking for the empty string to stop.
        for line in iter(fp.readline, ''):
            print(line, end='')

    # use regular iteration over the days using a single loop
    for day in days:
        print(day)

    #  using range and len for creating an index to use in the iteration
    for m in range(len(days)):
        print(m, days[m])

    # using enumerate reduces code and provides a counter (default start = 0)
    print('using enumerate:')
    for i, m in enumerate(days):
        print(i, m)

    # use zip to combine sequences (of same length).
    # when using diff length sequences, the zip terminates after the
    # shortest sequence is exhausted!
    for day_tuple in zip(days, days_spanish):
        print(day_tuple)

    # using enumerate indicating the start of the counter
    for index, day_tuple in enumerate(zip(days, days_spanish), start=1):
        print(index, day_tuple[0], "=", day_tuple[1], "in Spanish")


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# Sun
# Mon
# Tue
# This is line 1
# This is line 2
# This is line 3
# This is line 4
# This is line 5
# This is line 6
# Sun
# Mon
# Tue
# Wed
# Thu
# Fri
# Sat
# 0 Sun
# 1 Mon
# 2 Tue
# 3 Wed
# 4 Thu
# 5 Fri
# 6 Sat
# using enumerate:
# 1 Sun
# 2 Mon
# 3 Tue
# 4 Wed
# 5 Thu
# 6 Fri
# 7 Sat
# ('Sun', 'Dom')
# ('Mon', 'Lun')
# ('Tue', 'Mar')
# ('Wed', 'Mie')
# ('Thu', 'Jue')
# ('Fri', 'Vie')
# ('Sat', 'Sab')
# 1 Sun = Dom in Spanish
# 2 Mon = Lun in Spanish
# 3 Tue = Mar in Spanish
# 4 Wed = Mie in Spanish
# 5 Thu = Jue in Spanish
# 6 Fri = Vie in Spanish
# 7 Sat = Sab in Spanish
