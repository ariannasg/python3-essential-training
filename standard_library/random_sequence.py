#!usr/bin/env python3
import random
import string

# A common use case for random number generation is to use the generated
# random number along with a sequence of other values.
# So for example, you might want to select a random element from a list or
# a set of other elements.

# Use the choice function to randomly select from a sequence
moves = ["rock", "paper", "scissors"]
print(random.choice(moves))

# Use the choices function (introduced in python 3.6) to create a list of
# random elements
roulette_wheel = ["black", "red", "green"]
weights = [18, 18, 2]
# we define we want a list of 10 elements, otherwise is 1 by default
# there are only 2 green spaces on a roulette wheel, the green color shouldn't
# have the same chance to appear as black and red. we use weights for this.
# the weights arg tells the function how to distribute the results.
print(random.choices(roulette_wheel, weights, k=10))

# The sample function randomly selects elements from a population
# without replacement (the chosen items are not replaced)
# and without duplicates.
# here we print 6 random uppercase letters without duplicates
chosen = random.sample(string.ascii_uppercase, 6)
print(chosen)

# The shuffle function shuffles a sequence in place
players = ["Bill", "Jane", "Joe", "Sally", "Mike", "Lindsay"]
random.shuffle(players)
print(players)
# to shuffle an immutable sequence/collection, use the sample function first
result = random.sample(string.ascii_uppercase, k=len(string.ascii_uppercase))
random.shuffle(result)
print(''.join(result))

# CONSOLE OUTPUT (it will vary!):
# paper
# ['black', 'red', 'black', 'black', 'black', 'black', 'red', 'black', 'red', 'red']
# ['P', 'D', 'W', 'K', 'U', 'V']
# ['Lindsay', 'Mike', 'Bill', 'Sally', 'Joe', 'Jane']
# IRKXAVZNPHUCBLSEOJGQYWTFDM
