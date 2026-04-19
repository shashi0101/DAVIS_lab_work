## Program to sort 10 numbers in descending order (without using sort)

# Take input in one line (space separated)
nums = list(map(int, input("Enter 10 numbers: ").split(",")))

# Sorting (Descending)
n = len(nums)

for i in range(n):
    for j in range(n - i - 1):
        if nums[j] < nums[j + 1]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp

# Output
print("Sorted list in descending order:", nums)
