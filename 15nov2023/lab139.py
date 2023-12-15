# try except
# try:
# a= 10/0
#except xero division error as e:
#print(e)

#try except and nested except

try:
    num1 = int(input("enter the number"))
    num2 = int(input("enter the number"))
    result = num1/num2

except ValueError:
    print("Invalid error")

except ZeroDivisionError:
    print("Num2 is zero")

else:
    print(f"Result {result}")

finally:
    print("I will be always executed!!")

# num 1 - 10, pramod (ValueError)
# num 2 - 0

# ZeroDivisionError
# ValueError


# else and f