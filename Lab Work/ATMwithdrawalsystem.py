#to check the withdrawal in ATM
# ATM function
def atm():
    balance = 10000

    while True:
        print("\nCurrent Balance:", balance)
        
        amount = float(input("Enter withdrawal amount (0 to exit): "))
        
        # Exit condition
        if amount == 0:
            print("Thank you! Exiting...")
            break
        
        # Invalid amount
        if amount < 0:
            print("Invalid amount")
        
        # Insufficient balance
        elif amount > balance:
            print("Insufficient balance")
        
        # Successful withdrawal
        else:
            balance -= amount
            print("Withdrawal Successful")
            print("Remaining Balance:", balance)


# Call function
atm()