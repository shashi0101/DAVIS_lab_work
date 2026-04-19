# Convert list to tuple after removing duplicates

a = [1, 2, 2, 3, 4, 4]

# remove duplicates using set
unique = set(a)

# convert back to tuple
result = tuple(unique)

print(result)