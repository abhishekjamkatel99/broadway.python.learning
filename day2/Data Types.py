# Mutable and Immutable objects ####
"""
If an object once created can be changed later than the object is a mutable object

But if an object once created can never be changed throughout its life cycle then it is an immutable object.

List, dictionary, set are the example of Mutable object.
Numbers,Tuple, Boolean, string are the example of immutable object.
"""

a= [a,b,c]
a[1]='d'
a

b= (1,2,3)
b[1]=5 #