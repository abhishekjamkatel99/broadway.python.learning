# Sort() method is used to sort the elements of list in ascending or descending order and
# alphabetically for strings.
numbers = [7,3,4,1,8,6,2,5]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)




numbers =[(5,4),(3,2),(1,9),(6,1)]
# Expected Result [(6,1),(3,2),(5,4),(1,9)]


def sort_with_second_item(data):
    return data[1]


numbers.sort(key=sort_with_second_item)
print(numbers)

a = [(4,12,5),(6,1),(11,12),(6,7,8)]
#expected result [(6,1),(4,12,5),(6,7,8),(11,12)]


def sort_with_last_item(data):
    return data[-1]

a.sort(sort_with_last_item)
print(a)