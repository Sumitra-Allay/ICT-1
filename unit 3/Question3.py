#Create a program where the correct username is "admin" and the password is "12345" 
#The user gets only 3 attempts
#if correct, print "Login Successful" and stop
#if all attempts are used, print "Account Locked"
 
# Simple login system with 3 attempts

correct_username = "admin"
correct_password = "12345"
attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect credentials. {attempts} attempt(s) left.")
        else:
            print("Account Locked") 
#How it works:

#The program checks the entered username and password.
#If correct, it prints "Login Successful" and stops.
#If incorrect, it reduces the attempt count.
#After 3 failed attempts, it prints "Account Locked".
#If you’d like, I can also make a version that hides the password input so it’s not visible when typing. Would you like me to do that?

