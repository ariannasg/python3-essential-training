#!usr/bin/env python3


# Sorting simple data types such as numbers and strings can usually be done
# with just a regular sorted function. But for more complex types, such as
# custom objects we need to tell Python what property of the object to sort on.
# To do this, we  use the sort key parameter that the sorted function provides.
# the key parameter specifies a function that will be called for each object
# that is being sorted. This function returns the value of a particular
# property to use for the sort comparison.
class Product:
    def __init__(self, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount

    def __repr__(self):
        return repr((self.name, self.price, self.weight))

    def discount_price(self):
        return self.price - (self.price * self.discount)


# use the key parameter to select a field to sort on
def sort_prod(product):
    return product.price


prodList = [
    Product("Widget", 50, 10, 0.05),
    Product("Doohickey", 40, 8, 0.15),
    Product("Thingamabob", 35, 12, 0.0),
    Product("Gadget", 65, 7, 0.20)
]

# use a function as the key parameter to select a field to sort on
print(sorted(prodList, key=sort_prod))

# use an inline lambda function as the key parameter do the same as above
print(sorted(prodList, key=lambda p: p.price))

# the key parameter can also call a method on the object
print(sorted(prodList, key=lambda p: p.discount_price()))

# CONSOLE OUTPUT:
# [('Thingamabob', 35, 12), ('Doohickey', 40, 8), ('Widget', 50, 10), ('Gadget', 65, 7)]
# [('Thingamabob', 35, 12), ('Doohickey', 40, 8), ('Widget', 50, 10), ('Gadget', 65, 7)]
# [('Doohickey', 40, 8), ('Thingamabob', 35, 12), ('Widget', 50, 10), ('Gadget', 65, 7)]
