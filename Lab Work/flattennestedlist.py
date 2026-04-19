# Flatten a nested list (1 level)

nested = [[1, 2], [3, 4], [5]]

result = []

for i in nested:
    for j in i:
        result.append(j)

print(result)