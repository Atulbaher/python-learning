# Break and continue with the loops

# Break
# 1T 10 -> break when value of count = 5 -> 1,2,3,4,5,x

count = 1
while count <=10:
    count = (count + 1)
    print(count)
    if count >= 5:
        break
        print(count)

# i want to break when count = 5

for counter in range(1,10):
    print(counter)
    if counter == 5:
        break
        print(counter)

print(" for loop is end")
