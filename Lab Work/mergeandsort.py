# Merge two lists and return sorted unique elements

list1 = [3, 1, 2]
list2 = [2, 4, 5]

# combine and remove duplicates
result = list(set(list1 + list2))

# sort the result
result.sort()

print(result)