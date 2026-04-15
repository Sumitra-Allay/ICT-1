no_of_Students = int(input("Enter the number of students"))
i = 1 #initialize
student_names = {} #Empty dict to store the names of the students
while i <= no_of_Students: #conditions
    name = input("Enter the name of the student:")
    print("The name of student{} is {}".format(i,name))
    i+= 1 #increment the value of i by 1 in each iteration of loop
    student_names[i] = name #it adds the name of the studen to the dict
    #student_names with the key as the value of i

print(student_names) #it prints the dict student_names whiich the students names and number

while True :
    print("This is an infinite loop.Press Ctrl+c to stop it.") 

