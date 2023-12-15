#Abstraction - oops
# hiding the details and showing the what is required
#car - > start the engine - > put the gear - > start driving
# -> do you know how engine is started ? , how gear box was managed ?
# hide the implementation and show only the important details
# to represent complex systems by simplifying and hiding unnecessary details

#ABC -> ?  Abstract Base Class
# Abstract base method
# shape -> Rectangle , Circle
# shape - > perimeter , area
# Animal(speak) -> Dog, Cat, Tiger(Roar)


from abc import ABC , abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name

        @abstractmethod
        def sound(self):
            pass

class Dog(Animal):
    def sound(self):
        return "Bow Bow"

class Cat(Animal):
    def sound(self):
        return "Meow"

class Tiger(Animal):
    def sound(self):
        return "Roar Roar !!, Grrrr!!!!"


#dog= Dog()
#print(dog.sound())

cat = Cat()
print(cat.sound())

tiger = Tiger()
print(tiger.sound())



# animal = Animal()