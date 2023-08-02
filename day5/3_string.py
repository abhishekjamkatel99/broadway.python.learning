# Strings are immutable and sequence data-type in python
# Creating an empty string

a = "" # empty string
b = str() # empty string
c = '' # empty string
d= """""" # empty string

# Creating a non-empty string
a = "Hello world"
b = 'Python is a high level language'
c = """
Hello World.
Python is awesome
"""


# Quote characters
a ="I'am learning python"
b ='he said, "python is easy to learn"'

# We can also escape characters for in strings with quote
a= 'I/m learning Python'
b= "he said,\ "python is easy to learn\""

# Escape Characters are the characters in python which suppress  the actual python meaning and gives
# new meaning to that characters
# \',\",\n,\t etc arte the examples of escape characters

print('hello\nWorld') # Print Hello in first line and World in second line
print('hello\tWorld') # Print Hello in first, a tab, world

# Python as has Triple guoted strings
message = """
I'm learning python
"""

# There is no need for\' (escape characters) for triple quoted stings
# Triple quoted strings are not only used as normal strings, but also used to add code descriptions
# in functions, classes and as multiline comments

def addition(a,b):
    """

    :param a: any integer value
    :param b: any integer value
    :return: sum of a and b
    """


help(addition)
