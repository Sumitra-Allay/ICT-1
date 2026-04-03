my_set = {1,2,3,"Hello",3.14,1,2,False} #Duplicate values will be removed in as set
print(type(my_set)) #Data Type of my_set is set
print(my_set) #output:{False, 1, 2, 3.14, 3, 'Hello'} #Not:The order may vary
#my_set[0] = "Start" #This will raise an error becasue sets are unodered and do not support indexing. Additionally, sets are immutable
my_set.add("world")
print(my_set) #{False, 1, 2, 3.14, 3, 'world', 'Hello'}. The order may vary
my_second_set = {3,4,5}
union_set = my_set.union(my_second_set)
print(union_set) #{False, 1, 2, 3.14, 3, 4, 5, 'world', 'Hello'} #Note:the order may vary
intersection_set = my_set.intersection(my_second_set)
print(intersection_set)
difference_set = my_set.difference(my_second_set)
print(difference_set)
my_set.clear()
print(my_set)