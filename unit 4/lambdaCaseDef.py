#Conditiion Checking: A lambda function can use comditional expression(if-else) to return different results based on a condition
even_odd = lambda x: "Even" if x%2 == 0 else "odd"
num = int(input("Enter a number:"))
print(even_odd(num)) 