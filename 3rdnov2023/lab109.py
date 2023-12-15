# car -
# object - Tesla, Lambo

class Car:
    name = None
    colour = None
    model = None
    speed = None
    engine = None

    # self is a special variable that is used within the context of
    # object-oriented programming (OOP).
    # It is a reference to the instance of a class
    # access and manipulate the attributes and methods of that instance / Object

    def start_engine(self):
        print("starting engine")

    def drive(self):
        print("drive")

    def car_break(self):
        print("break")

    def who_is_driving(self):
        print("I am driving - >" + self.name)


tesla_obj_ref = Car()
lambo_obj_car = Car()

tesla_obj_ref.name = "Tesla"
lambo_obj_car.name = " Lambo"

tesla_obj_ref.who_is_driving()
lambo_obj_car.who_is_driving()
