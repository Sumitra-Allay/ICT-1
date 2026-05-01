#1.Conditiion Checking: A lambda function can use comditional expression(if-else) to return different results based on a condition
even_odd = lambda x: "Even" if x%2 == 0 else "odd"
num = int(input("Enter a number:"))
print(even_odd(num)) 

#2.Return Multiple results:it can return multiple results by combining them into a tuple
arith = lambda x,y: (x+y, x-y, x/y)
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
print(arith(num1,num2))

#3.filter(): filter() uses a lambda expression to select elements from a list that satisfy a given condition
mylist = [1,2,3,4,5,6]
even = filter(lambda x: x %2 == 0,mylist)
print(list(even))

#4.map(): map() function applies a lambda expression to each element and return a map object
mylist = [1,2,3,4]
double = map(lambda x : x*2, mylist)

#convert it bcak
mynewlist = (list(double))
print(mynewlist)
division= map(lambda x : x/2, mynewlist)
print(list(division))

#5.reduce() : reduce() function repeatedly applies a lambda expression to elements of a list to combine them into a single result
from functools import reduce
mylist = [1,2,3,4]
mul = reduce (lambda x, y: x*y, mylist)
print(mul)

#implememt create a lambda function for the following 
# #a.To check whether a number is positive,negative or zero
num = int(input("Enter a number:"))
check = lambda x: "Positive" if x >0 else "negative" if x<0 else "Zero" 
print(check(num))  
