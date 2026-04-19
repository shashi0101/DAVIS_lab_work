#to print the pattern
# Number of rows
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    
    # Check even or odd row
    if i % 2 == 0:
        symbol = "*"
    else:
        symbol = "#"
    
    # Print pattern
    for j in range(i):
        print(symbol, end=" ")
    
    print()  # next line