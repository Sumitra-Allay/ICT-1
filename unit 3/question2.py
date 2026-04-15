#sum until zero: write a program that keeps taking integra input from the user and adds them to total. Stop when the user enters 0. Finally, print the total sum.
total = 0
while True:
    num = int(input("Enter an integer (0 to stop): "))
    
    if num == 0:
        break  # <-- This exits the loop
    
    total += num 