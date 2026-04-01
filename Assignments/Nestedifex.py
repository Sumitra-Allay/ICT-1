age = int(input("Enter your age"))
if age >= 18:
    registered_voter = input("Are you a registered voter? (True/False:")
    registered_voter = registered_voter.lower()
    if registered_voter == "True":
        print("You are eligible to vote.")
    else:
         print("You need to registered to vote.") 
else:
    print("You are not eligible to vote.")          