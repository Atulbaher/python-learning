# Multi level Inheritance
# level - GF - > F - > S

class Grandparent:
    def grandparent_method(self):
        return "Grandparent's method"


class Parent(Grandparent):
    def parent_method(self):
        return "Parents method"


class Child(Parent):
    def child_mathod(self):
        return "Child's Method"


child = Child()
print((child.grandparent_method()))
print(child.parent_method())
print(child.child_mathod())
