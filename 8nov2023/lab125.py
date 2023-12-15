# Hybrid Inheritance

# multiple types of inheritance, such as single, multiple, and multilevel inheritance.

class A:
    def methodA(self):
        return "MethodA"

class B(A):
    def methodB(self):
        return "MethodB"

class C(A):
    def methodC(self):
        return "MethodC"

class D(B,C):
    def methodD(self):
        return "MethodD"

d = D()
print(d.methodD())
print(d.methodC())
print(d.methodB())
print(d.methodA())