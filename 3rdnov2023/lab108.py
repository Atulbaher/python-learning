# Class and Object in Python.

# Person
# Attributes - name,age, phone_no, height, weight, gender, prof
# Methods - Can do -> Run(), sleep(). sing(), talk(), eat(), fight(), learn(), hear(), think()


# Objects
# Amit
# Durga - GENDER  - fEMALE
# Santosh -

class Person:
    name = None
    age = None
    phone_no = None
    height = None
    weight = None
    gender = None
    prof = None

    def talk(self):
        print("talk")

    def sleep(self):
        print("sleep")

    def walk(self):
        print("i m walking")


atul_object = Person()
atul_object.name = "atul"
atul_object.age = 34
atul_object.phone_no = "987654321"

print(atul_object)
atul_object.sleep()

mitu_obj = Person()
mitu_obj.name = "mitu"

print(mitu_obj)
mitu_obj.sleep()