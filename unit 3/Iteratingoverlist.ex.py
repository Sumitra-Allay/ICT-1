li = ["Python Programming","Python Fundamental","Python Interview Questions"]
for x in li:
    print (x)
lenli = len(li) #len()returns the number of items in the list li i.e.3. This value is stored in the variable lenli
for x in range(lenli): #x is a variable that takes the value of each index
    print(li[x])

new_tuple = tuple (li)
for x in new_tuple:
    print(x)
lennew_tuple = len(new_tuple)
for x in range(lennew_tuple):
    print(new_tuple[0])

new_set = set (li)
for x in new_set:
    print(x)



