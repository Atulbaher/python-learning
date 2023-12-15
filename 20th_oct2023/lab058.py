# Match
# Similar to Switch in Java

number = int(input("enter a number\n"))

match number:
    case 1:
        print("you entered 1")
    case 2:
        print("you entered 2")
    case 3:
        print("you entered 3")
    case _:
        print("no idea")
