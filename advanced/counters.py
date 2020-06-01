#!usr/bin/env python3
from collections import Counter


# one of the common uses of dictionaries is to keep track of the count of
# individual items. the collections modules supplies a counter class which is
# a dictionary subclass for counting hashable objects.
# if need a class to help keep track of a number of different items, along
# with a set of operations for working on the data or multiple sets of data
# such as the most common word; the counter class might be a good fit.
def main():
    # list of students in class 1
    class1 = ["Bob", "James", "Kevin", "James", "Frank"]
    print(class1)

    # list of students in class 2
    class2 = ["Bill", "Barry", "Frank", "Gabby", "Kelly", "James", "Joe"]
    print(class2)

    # Create a Counter for class1 and class2
    c1 = Counter(class1)
    print(c1)
    print(sorted(c1.elements()))
    print(c1.values())
    c2 = Counter(class2)
    print(c2)

    # How many students in class 1 named James?
    print('there are', c1["James"], 'students called James in class 1')

    # How many students are in class 1?
    print('there are', sum(c1.values()), "students in class 1")

    # We can combine the two classes
    c1.update(class2)
    print(c1)
    print('there are', sum(c1.values()), "students in class 1 and 2")

    # What's are the most 3 common names in the two classes?
    print(c1.most_common(3))

    # Separate the classes again
    c1.subtract(class2)
    print(c1)
    # What's the most common name in class 1?
    print(c1.most_common(1))

    # Intersection of both counters, what items are present in the two classes
    print(c1 & c2)

    # Calculating the most common 5 letter name in class 1
    five_letter_names = list(filter(lambda word: len(word) == 5, class1))
    print(five_letter_names)
    print(Counter(five_letter_names).most_common(1))
    print(Counter(five_letter_names).most_common(1)[0][0])


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# ['Bob', 'James', 'Kevin', 'James', 'Frank']
# ['Bill', 'Barry', 'Frank', 'Gabby', 'Kelly', 'James', 'Joe']
# Counter({'James': 2, 'Bob': 1, 'Kevin': 1, 'Frank': 1})
# ['Bob', 'Frank', 'James', 'James', 'Kevin']
# dict_values([1, 2, 1, 1])
# Counter({'Bill': 1, 'Barry': 1, 'Frank': 1, 'Gabby': 1, 'Kelly': 1, 'James': 1, 'Joe': 1})
# there are 2 students called James in class 1
# there are 5 students in class 1
# Counter({'James': 3, 'Frank': 2, 'Bob': 1, 'Kevin': 1, 'Bill': 1, 'Barry': 1, 'Gabby': 1, 'Kelly': 1, 'Joe': 1})
# there are 12 students in class 1 and 2
# [('James', 3), ('Frank', 2), ('Bob', 1)]
# Counter({'James': 2, 'Bob': 1, 'Kevin': 1, 'Frank': 1, 'Bill': 0, 'Barry': 0, 'Gabby': 0, 'Kelly': 0, 'Joe': 0})
# [('James', 2)]
# Counter({'James': 1, 'Frank': 1})
# ['James', 'Kevin', 'James', 'Frank']
# [('James', 2)]
# James
