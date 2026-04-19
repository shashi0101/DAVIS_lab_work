#to classify the number  is positive, negative, zero, even or odd
# Function to classify number
def classify_number(num):
    
    # Positive / Negative / Zero
    if num > 0:
        print(num, "is Positive")
    elif num < 0:
        print(num, "is Negative")
    else:
        print(num, "is Zero")
    
    # Even / Odd (Nested if)
    if num != 0:   # zero ke liye even/odd avoid karne ke liye (optional)
        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")
    
    print()  # line gap for clarity


# Taking list input (space separated)
nums = list(map(int, input("Enter numbers: ").split()))

# Loop to process all numbers
for num in nums:
    classify_number(num)