#list is mutable, its contant can be changed...

my_list = [1,2,3,4,5,5]
print(my_list)
my_list[1] = 20
print(my_list)
print(type(my_list))

#tuple- it is immutable in nature...no modification

car = ("ford gt","raptor","lambo","lambo")
car2 = ("ford gt","True","lambo")
print(car)
print(type(car))
print(car2)
print(type(car2))


#car[1] = "xuv500"

print(len(car))

#tuple (), its cintant cant be changed, list[] and it contant can be changed!!

#list can be converted
list1 = [1,2,3,4,5,6,]
print(tuple(list1))
