#!usr/bin/env python3


# Python built-in sorting algorithms guarantee that sorts are stable.
# This means that when multiple objects are being sorted and they have the
# same key value, the original order in the data list is preserved.
# sorting stability guarantees that objects with the same key will
# have their order preserved even after the data is sorted
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


prodList = [
    Product("Doohickey", 40, 10, 0.15),
    Product("Widget", 50, 10, 0.05),
    Product("Doohickey", 40, 8, 0.15),
    Product("Thingamabob", 35, 12, 0.0),
    Product("Gadget", 65, 7, 0.20)
]

print(sorted(prodList, key=lambda p: p.price))

# sort by two different keys, taking advantage of stability
result = sorted(prodList, key=lambda p: p.weight)
print(result)
print(sorted(result, key=lambda p: p.price, reverse=True))

# CONSOLE OUTPUT:
# [('Thingamabob', 35, 12), ('Doohickey', 40, 10), ('Doohickey', 40, 8), ('Widget', 50, 10), ('Gadget', 65, 7)]
# [('Gadget', 65, 7), ('Doohickey', 40, 8), ('Doohickey', 40, 10), ('Widget', 50, 10), ('Thingamabob', 35, 12)]
# [('Gadget', 65, 7), ('Widget', 50, 10), ('Doohickey', 40, 8), ('Doohickey', 40, 10), ('Thingamabob', 35, 12)]
