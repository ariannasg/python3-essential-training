#!usr/bin/env python3


# Use special methods to compare objects to each other
class Employee:
    def __init__(self, fname, lname, level, yrs_service):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.yrs_service = yrs_service

    def __repr__(self):
        return f'{self.fname} {self.lname}'

    # implement comparison functions by employee level & yrs_service
    def __ge__(self, other):
        if self.level == other.level:
            return self.yrs_service >= other.yrs_service
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.yrs_service > other.yrs_service
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.yrs_service < other.yrs_service
        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.yrs_service <= other.yrs_service
        return self.level <= other.level

    def __eq__(self, other):
        return self.level == other.level


def main():
    # define some employees
    dept = [Employee("Tim", "Sims", 5, 9),
            Employee("John", "Doe", 4, 12),
            Employee("Jane", "Smith", 6, 6),
            Employee("Rebecca", "Robinson", 5, 13),
            Employee("Tyler", "Durden", 5, 12)]

    # Who's more senior?
    print('is Tim more senior than Jane?', bool(dept[0] > dept[2]))
    print('is Tyler less senior than Rebecca?', bool(dept[4] < dept[3]))

    # sort the items
    employees = sorted(dept)
    print('Sorted employees:')
    print(employees)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# is Tim more senior than Jane? False
# is Tyler less senior than Rebecca? True
# Sorted employees:
# [John Doe, Tim Sims, Tyler Durden, Rebecca Robinson, Jane Smith]
