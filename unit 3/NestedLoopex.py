for i in range(1,4) : #outer loop iteration from 1 to 3
    for j in range(i): #inner loop iterates from 0 to i-i
        print(f"Outer Loop iteration {i}, inner loop iteration {j+1}")  

for i in range(4):
    for j in range(i):
        print("*",end = "")
    print()