#!usr/bin/env python3
from operator import attrgetter, methodcaller, itemgetter


# the operator module functions provide easy ways to select fields
# attrgetter() retrieves a given attribute or property from an object
# itemgetter() retrieves an item at a given index in a collection
# methodcaller() calls the given method on the object
class Product:
    # i'm using the keyword only arg to enforce calling by keyword in prod_list
    def __init__(self, *, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount

    def __repr__(self):
        return repr((self.name, self.weight, self.discount_price()))

    def discount_price(self):
        return self.price - (self.price * self.discount)


prod_list = [
    Product(name="Widget A", price=50, weight=10, discount=0.05),
    Product(name="Widget B", price=40, weight=8, discount=0.15),
    Product(name="Widget C", price=35, weight=12, discount=0.0),
    Product(name="Widget D", price=65, weight=7, discount=0.20),
    Product(name="Widget E", price=70, weight=7, discount=0.12)
]

print("Using the attrgetter method:")
print(sorted(prod_list, key=attrgetter("weight"), reverse=True))

print("Using methodcaller to invoke a method:")
print(sorted(prod_list, key=methodcaller("discount_price")))

# Use itemgetter to retrieve an index
# inventory list of tuples of product name and number of items
inventory = [("Widget A", 5), ("Widget B", 2), ("Widget C", 4),
             ("Widget D", 7), ("Widget E", 4)]

# sort in order according to the 1st index of each of the tuple
print(sorted(inventory, key=itemgetter(1)))

# CONSOLE OUTPUT:
# Using the attrgetter method:
# [('Widget C', 12, 35.0), ('Widget A', 10, 47.5), ('Widget B', 8, 34.0), ('Widget D', 7, 52.0), ('Widget E', 7, 61.6)]
# Using methodcaller to invoke a method:
# [('Widget B', 8, 34.0), ('Widget C', 12, 35.0), ('Widget A', 10, 47.5), ('Widget D', 7, 52.0), ('Widget E', 7, 61.6)]
# [('Widget B', 2), ('Widget C', 4), ('Widget E', 4), ('Widget A', 5), ('Widget D', 7)]
