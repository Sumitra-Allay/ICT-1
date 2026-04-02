my_tuple = ('Hellow', 123456)
print(type(my_tuple))
print(my_tuple)
print(my_tuple[1])  #-1/1
a, b = my_tuple    #a = Hellow and b = 123456
print(b)
new_tuple = tuple(a)
print(new_tuple)    #'H', 'e', 'l', 'l', 'o', 'w'
concatenated_tuple = my_tuple + new_tuple
print(concatenated_tuple)  # 'Hellow',123456, 'H', 'e', 'l', 'l', 'o', 'w'
print(concatenated_tuple[2:6:2]) #'H', 'l'
print(concatenated_tuple[::-1]) #'w', 'o', 'l', 'l', 'e', 'H', 123456, 'Hellow'
del my_tuple
print(my_tuple) 
