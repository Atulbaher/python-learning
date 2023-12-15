# Take a input from user we eill create how

class Car:
    colour = None
    model = None

    def car_details(self):
        print("your car details is", self.colour, self.model)


car_colour = input("enter your car colour")
car_model = input("enter your car model")

car_obj_ref = Car()

car_obj_ref.colour = car_colour
car_obj_ref.model = car_model

# Obj ref we can call the function

car_obj_ref.car_details()

# car_details()
