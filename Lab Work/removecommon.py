#to remove common elements from the following lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5]

result = list(set(list1) - set(list2))

print(result)