# compare two numbers:

num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))

result = "greater then" if num1 > num2 else "less then" if num1 < num2 else "equal to"

print(f"{num1}is {result} {num2}")