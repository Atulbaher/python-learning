## poly
#abc
#exception
#polymorphism - object - oriented programing (oop)
# object -> belive differently based on the sti
#person -> amit, pramod -> talk (), amit can talk in hindi, pramod can talk in english

class Shape:
    def area(self):
        print("Area of shape")


class Rectangle(Shape):
    def __init__(self,lenght,width):
        self.length = lenght
        self.width = width

    def area(self):
        super().area()

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius

Shape1 = Rectangle(3 ,4)
print((Shape1.area()))

Shape2 = Circle(10)
print(Shape2.area())

Shape3 = Shape()
Shape3.area()