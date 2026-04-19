t#to create menu driven calculator
# Functions for operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Main program
while True:
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))#enter choice
    
    if choice == 5:
        print("Exiting Calculator...")
        break
    
    if choice >= 1 and choice <= 4:
        num1 = float(input("Enter first number: "))  #taking input
        num2 = float(input("Enter second number: "))
        
        if choice == 1:
            print("Result:", add(num1, num2))
        
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        
        elif choice == 4:
            print("Result:", divide(num1, num2))
    
    else:
        print("Invalid choice, try again")