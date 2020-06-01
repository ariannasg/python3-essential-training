#!usr/bin/env python3

# Use standard library functions to search strings for content
sample_str = "The quick brown fox jumps over the lazy dog"

# startsWith and endsWith functions
print(sample_str.startswith("The"))
print(sample_str.startswith("the"))
print(sample_str.endswith("dog"))


# the find function starts searching from the  left/start side of the str)
# and rfind function starts searching from the right hand-side of the str
# they both return the index at which the substring was found
print(sample_str.find("the"))
print(sample_str.rfind("the"))

# for knowing if a substr is contained in the str
print("the" in sample_str)


# using replace
new_str = sample_str.replace("lazy", "tired")
print(new_str)


# counting instances of substrings
print(sample_str.count("over"))

# CONSOLE OUTPUT:
# True
# False
# True
# 31
# 31
# True
# The quick brown fox jumps over the tired dog
# 1
