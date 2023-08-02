message = "hello world"


########## String Methods ###########
# Capitalize()

result = message.capitalize()
print(result)


# Title()
result = message.title()
print(result)

# Upper ()
result = message.upper()
print(result)

# lower()
result = message.lower()
print(result)



# String()
message = "hello world"
result = message.split()
print(result)  # ["Hello", "world"]

result = message.split('o')
print(result)  # ["Hell", "w", "rld"]

message = "I'm learning python"
result = message.split(',')
print(result)  # ["I","am", "learning","python"]


# Join()
message = ["I","am", "learning","python"]
result = " ".join(message)
print(result) # I am learning python


# message.join(" ") # this raises error

# result ==> I, am, learning, python
result = ", ".join(message)
print(result)



# Find()
message = "hello World"
result = message.find("wor")
print(result)  # 2

result = message.find("Wor")
print(result)  # -1


# Replace()
message = "hello world"
result = message.replace("hello","HELLO")






