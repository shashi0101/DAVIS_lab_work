# Find common elements in three lists

a = [1, 2, 3]
b = [2, 3, 4]
c = [2, 5, 3]

result = list(set(a) & set(b) & set(c))

print(result)