# Add() method
s = {1, 2, 3}
result = s.add(4)
print(result)  # None ; because add() method returns nothing
print(s)

# update() method
s = {1, 2, 3}
s.update([4, 5, 6, 7, 8])
print(s)   # {1, 2, 3, 4, 5, 6, 7, 8}

# discard
s = {1, 2, 3, 4}
s.discard(3)
print(s)  # {1, 2, 4}
s.discard(5)  # It doesn't raise error

# Remove()
s = {1, 2, 3, 4}
s.remove(2)
# s.remove(5) # It raises error

#  Clear()
s = {1, 2, 3, 4}
s.clear()
print(s)  # {}


# pop()
s = {1, 2, 3, 4}
print(s.pop())  # It randomly pops out any one value of the set.


# difference()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.difference(b)  # a -b
print(result)  # {1, 2}


# intersection()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.intersection(b))  # {3, 4}


#  Union()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))  # {1, 2, 3, 4, 5, 6}
print(a | b)  # | is used for union






# Isdisjoint()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.isdisjoint(b))  # False





# issubset()
a = {1, 2, 3, 4}
b = {2, 3}
print(b.issubset(a))  # True
print(a.issuperset(b))  # False


# symmetric difference
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.symmetric_difference(b)
print(result)  # {1, 2, 5, 6}

# symmetric difference update
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.symmetric_difference_update(b)
print(result)  # None
print(result)  # {1, 2, 5, 6}


#





