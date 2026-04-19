#to check the login credentials
# Login function
def login():
    correct_username = "admin"
    correct_password = "1234"
    
    attempts = 0
    
    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username == correct_username and password == correct_password:
            print("Login Successful")
            return   # exit function
        
        else:
            print("Wrong credentials")
            attempts += 1
    
    print("Account Locked")


# Call function
login()