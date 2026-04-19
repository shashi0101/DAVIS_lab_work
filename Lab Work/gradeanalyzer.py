#to analysis the grade of students according to their marks
# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"


# Loop for 5 students
for i in range(5):
    marks = int(input(f"Enter marks of student {i+1}: "))
    
    grade = calculate_grade(marks)
    
    print(f"Student {i+1} Grade:", grade)