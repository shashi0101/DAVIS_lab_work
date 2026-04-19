a = [10, 20, 30, 40, 50]
k = 2

k = k % len(a)   # handle large k

result = a[-k:] + a[:-k]

print("Rotated list:", result)