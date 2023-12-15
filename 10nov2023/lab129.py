# method overriding - same name in the parent and child
# child always overide the parent function

class Animal:
    def __init__(self):
        pass

    def sound(self):
        print("Animal Sound")


class Dog(Animal):
    def __init__(self):
        pass

    def sound(self):
        super().sound()
        print("Dog sound")


animal1 = Animal()
animal1.sound()

dog = Dog()
dog.sound()
