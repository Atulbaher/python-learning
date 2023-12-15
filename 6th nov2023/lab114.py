class Person:

    def __init__(self):
        print("can i use you?")

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("you created an object with name and age")

    def printDetails(self):
        print("your details are",self.name,self.age)

    def printDetails2(self):
        print("your details are",self.name*2)

amit = Person("amit",34)
amit.printDetails()


nikhil1 = Person("nikhil",45)
nikhil1.printDetails()


amit.printDetails2()
nikhil1.printDetails2()