# Remove empty sets from list

a = [{1, 2}, set(), {3, 4}, set()]

result = []

for i in a:
    if i:   # empty set = False
        result.append(i)

print(result)