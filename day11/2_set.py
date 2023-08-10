# Set in python are mutable. However, every element of set must be immutable.
# Creating an empty set
a = set()  # This is proper way of creating an empty set
# a = {} # This is not an empty set rather it is a dictionary

# Creating non empty set
a = ([1, 2, 3, 4])
print(a)  # {1, 2, 3, 4}

a = {1, 2, "a", "b", "apple", True}
print(a)

# Set only take unique element
print(set([1, 2, 3, 1, 3, 3,]))
