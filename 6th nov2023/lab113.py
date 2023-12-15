class Car:
    name = "Atul" # clas variable

    def __init__(self,make,model):#default con
        self.make = make#instance Varriable
        self.model=model#instance Varriable
        print("I will be called first")

    def start_engine(self):
        print("starting a car", self.make,self.model)

car1 = Car("Toyota","Camry")
car2 = Car("Honda","civic")

car1.start_engine()
car2.start_engine()

print(id(car1))
print(id(car2))


# Object is created a Special Function is called automatically __int__()
# All the attribute Object you can initilize - add some initial value to them