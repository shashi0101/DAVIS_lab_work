#to calculate in bonus in employees salary
# Function to calculate bonus
def calculate_bonus(salary, experience):
    
    if experience >= 10:
        bonus = salary * 0.20
    elif experience >= 5:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05
    
    total_salary = salary + bonus
    
    print("Bonus:", bonus)
    print("Total Salary:", total_salary)
    print()


# Loop for multiple employees
n = int(input("Enter number of employees: "))

for i in range(n):
    print(f"\nEmployee {i+1}:")
    
    salary = float(input("Enter salary: "))
    experience = int(input("Enter years of experience: "))
    
    calculate_bonus(salary, experience)