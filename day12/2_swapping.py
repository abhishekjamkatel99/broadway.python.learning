a = 2
b = 4

print(a)  # 2
print(b)  # 4

# Creating a temporary variable 'temp'
temp = a
a = b
b = temp
print(a)  # 2
print(b)  # 4


a = 2
b = 4

print(a)
print(b)

a, b = b, a
print(a)  #   4
print(b)   #   2


