#program for tail implementation
#algorithm:--
# #Start
#Take N from user
#Open file in read mode
#Read all lines
#Get last N lines
#Display them
#Stop

#taking input from user
n = int(input("Enter number of lines: "))
#open file in read mode
with open("file.txt", "r") as file:
    lines = file.readlines()

for line in lines[-n:]:
    print(line.strip())