# find the maximum of three numbers using the ternary operators:

num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))
num3 = float(input("enter the third number"))
max_number = num1 if (num1 > num2 and num3) else (num2 if num2 > num3 else  num3)



max_number = num1 if (num1 > num2 and num3) else (num2 if num2 > num3 else num3)
print(f"the maximum of {num1},{num2},{num3} is {max_number}")