#write the program to reverse the content of file
#algoritm:--
#Start
#Read all lines
#Reverse order
#Write into new file
#Stop
#open file in read mode
with open("input.txt", "r") as file:
    lines = file.readlines()
#open file in write mode
with open("reverse.txt", "w") as out:
    for line in reversed(lines):
        out.write(line)