#Operators are the special symbols in any programing language to carry out
# Arithmetic and logical Operations

a=1
b=2
c=1+2
#Here '='is an assignment operator anf '+' is an arithmetic operation

# Arithmetic Operators
# Addition [+]
# Subtraction [-]
# Multiplication [*]
# Division [/]
# Floor Division [//] => Floor division removes the decimal value and only
# provides the integer towards floor.
print (3//2) # it gives 1
print(-3//2) #It gives -2

# Exponential (**)
print (3**2) #It gives 9

# modulus (%) => Gives 1
print(3%2) # it gives 1
print(4%2) # it gives 0



##### Comparison / Relational operations #####
# ==, <,>,




# logical operators
# and, or , not are the logical operators and their operators are "and", "or" and "not" respectively.
# The results in logical operations are either True or False.




# Identity Operators()
# Identity operators check whether the two objects are same or not. 'is' and 'is not' are used for the identity check.
a=1
b=1
print(a is b) # true
print(id(a))
print (id(b)) # for the sane object, id() gives equal value


# membership operators
# it is used to check membership of an object in a sequence
# used for membership check
print(2 in [1,2,3]) # true
print(3 is notin [1,2,3]) # false


# Assignment operator
# The result of any operation can be assigned to a variable to a variable using an assignment
# operator, "=" is a basic assignment operator.
name = "jon" #here = is an assignment operator.

# +=,_=,*=,/= are also some of the assignment operators
a=1
a= a+1 # this line can also be written as a +=1
print(a) #2
a+=1 #3
print(a)



# precedence and associativity
# Precedence of the operators is the rule that determines which operators should be executed first
# if multiple operators in an operation have the same precedence then the associative determines the operation sequence.


# Normally associativity is form left-right  expect for the case '**'.
# For exponent (**), it is from right-left

print(2**3**2) #512





