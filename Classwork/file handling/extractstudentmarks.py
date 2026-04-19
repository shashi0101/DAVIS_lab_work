# Program to extract students with marks > 75
#algorithm:
#start
#open the file student.txt 
#openStart
#Open the file student.txt in read mode
##Read each line from the file
#Split the line into name, marks, city
#Convert marks into integer
#Check if marks > 75
#If yes → write that record into new file
#Repeat steps 4–7 for all lines
#Close both files
#Display message “Data extracted successfully”
#Stop
# Program to extract students with marks > 75

# Open files
with open("student.txt", "r") as source:
    with open("result.txt", "w") as destination:
        
        # Read each line
        for line in source:
            data = line.strip().split(",")
            
            name = data[0]
            marks = int(data[1])
            city = data[2]
            
            # Condition check
            if marks > 75:
                destination.write(line)

print("Data extracted successfully!")







































# Open files
with open("student.txt", "r") as source:
    with open("result.txt", "w") as destination:
        
        # Read each line
        for line in source:
            data = line.strip().split(",")
            
            name = data[0]
            marks = int(data[1])
            city = data[2]
            
            # Condition check
            if marks > 75:
                destination.write(line)

print("Data extracted successfully!")