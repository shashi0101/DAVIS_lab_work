#to check whether the number is palindrome or not
# Function to check palindrome
def is_palindrome(value):
    
    original = str(value)
    reversed_str = ""
    
    # Reverse using loop
    for ch in original:
        reversed_str = ch + reversed_str
    
    # Check palindrome
    if original == reversed_str:
        print(value, "is a Palindrome")
    else:
        print(value, "is NOT a Palindrome")


# Take input
data = input("Enter a number or string: ")

# Call function
is_palindrome(data)