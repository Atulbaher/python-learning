# Inheritance
#(single Inheritance)

# Parent - Child
# Father - > son
# GF - > F - > s
# 1bhk -> 1bhk -> 1bhk ->

# Single Inheritance

class Animal:
    def car(self):
        print("Lambo")
    def speak(self):
        print("Animal speak!")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()