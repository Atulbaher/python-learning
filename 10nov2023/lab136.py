a = int(input("Enter your A number"))
b = int(input("Enter your B number"))

try:
    c = a/b
    print(c)

except Exception as error:
    print(" you are driving the value of A with zero, please dont do it",error)