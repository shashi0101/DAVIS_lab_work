# program to check age using exception

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise Exception("Not eligible (Age must be 18+)")
    else:
        print("Eligible")
        
except Exception as e:
    print("Error:", e)