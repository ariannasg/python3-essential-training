#!usr/bin/env python3
import bisect

# use the bisect functions to maintain a list in sorted order during the
# insertion of new elements.
# the bisect, bisect right, and bisect left functions will determine the index
# at which a given value should be inserted to maintain order.
# Bisect and bisect right are essentially synonyms for each other and
# they will return the index to the right side of an element that's already in
# the array if it matches the one we're supplying.
values = [5, 7, 13, 20, 25, 31, 36, 43, 47, 49, 50, 75]

# exercise the left and right bisection routines
# they return the index at which the new 25 should be added
print(bisect.bisect(values, 25))
print(bisect.bisect_right(values, 25))
print(bisect.bisect_left(values, 25))

# use insort to insert new items
bisect.insort_right(values, 25)  # will insert to the right
print(values)
bisect.insort(values, 24)
print(values)


def calculate_grade(score):
    # use the bisect function to identify cutoff points for the letter grades
    index = bisect.bisect(breakpoints, score)
    return grade_letters[index]


# bisect can be used as an array lookup using breakpoints
breakpoints = [60, 70, 80, 90]
grade_letters = 'FDCBA'
scores = [81, 68, 53, 91, 90, 82, 76, 71, 84]
print(scores)

results = [calculate_grade(score) for score in scores]
print(results)

# CONSOLE OUTPUT:
# 5
# 5
# 4
# [5, 7, 13, 20, 25, 25, 31, 36, 43, 47, 49, 50, 75]
# [5, 7, 13, 20, 24, 25, 25, 31, 36, 43, 47, 49, 50, 75]
# [81, 68, 53, 91, 90, 82, 76, 71, 84]
# ['B', 'D', 'F', 'A', 'A', 'B', 'C', 'C', 'B']
