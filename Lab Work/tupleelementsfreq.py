# Count frequency of elements in tuple

t = (1, 2, 2, 3, 1, 4)
freq = {}

for i in t:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequency:", freq)