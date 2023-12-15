# public -  varriable - don't mention anything
# Protected- _
# Private - __

# Variable and function

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name == "John":
            print("Don't set the name")
        else:
            self.__name == name

    def print_details(self):
        print("your details", self.__name, self.__age)


person = Person("Atul", 34)  # it will call the __init__ with name, age
person.print_details()

#print(persom.__name) #private ?

#how to change it Get and Set ?
# Fetch - Get
# set the Value - construction

person.set_name("John")

name = person.get_name()
print(name)

person.print_details()