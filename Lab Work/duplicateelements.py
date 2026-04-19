a = [1, 2, 3, 2, 4, 5, 1]

duplicates = []
#
for i in a:
    if a.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate elements:", duplicates)