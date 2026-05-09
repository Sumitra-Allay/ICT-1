file = open('Students.xlxs', 'w')
file.write("Name, ID\n")
file.write("Ghalley, 001\n")
file.write("Lepcha, 002\n")
file.write("Momo, 003\n")
file.write("Halay, 004\n")
file.write("Dazzling, 005\n")
file.close()
file = open('Students.xlxs', 'r')
students = file.read()
print(students)
file.close()
searchN = input("Enter a name to search: ")
found = False
with open('Students.xlxs', 'r') as file:
    for student in file:
        if searchN.lower() in student.lower():
            print(student)
            found = True
            break
if not found:
    print("Name not found in the file.")
print() 