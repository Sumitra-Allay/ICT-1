#Information Management System of student
students=[] # save names of student in the list
student_data={} # save students detail in dictionary(dict)

# add student details
name=input("Enter name of the student: ") #add the student name
age=input("Enter age: ") #Enter the age of the student
grade=input("Enter grade: ") #Enter the grade of the student

#check in if studen exit and add the student name
if name in student_data: #Checking the name of the student exist
    print("Student already exists!") #Print "Student already exists" if name of student is the student list
else:
    students.append(name) #Add the name
    student_data[name]={"age": age, "grade": grade} #add grade and age of the student
    print("Student added successfully") #print "Student added successfully"

# displaying all students and their details
if (student_data): #to check in the details of the student
    print("No students found.") #print "Sorry,No students found." if student not found by the name
else:
    for name in student_data: #Print the students details
        print("Name:", name) # Enter the name of the students 
        print("Age:", student_data[name]["age"]) #Enter the age of the student
        print("Grade:", student_data[name]["grade"]) #Enter the grade of the student

# search the students
search=input("Enter name of the student to search: ") #Enter name of student to search

if search in student_data:
    print("Student found!") #If student name found print "Student found"
    print("Name:", search) #Enter name of the student to search
    print("Age:", student_data[search]["age"]) #Enter age of the of the student
    print("Grade:", student_data[search]["grade"]) #Enter of the student
else:
    print("Student not found.") #Print "Sorry,Student not found." if student not found

# remove student 
remove_name = input("Enter name of the student to remove: ") #Enter name of the student to remove

if remove_name in student_data: 
    students.remove(remove_name) #remove the student of the name
    del student_data[remove_name] #Permanently removing the student from student data (student dict)
    print("Student removed successfully.") #Print "Student removed successfully." after removing it
else:
    print("Student not found.") #Display "Student not found." after removing 