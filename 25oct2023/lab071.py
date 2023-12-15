# list - cillection of item ( Duplicate is allowed)

my_list = [ 1, 2, 3]
my_list2 = [1, True, "atul", 12.34 ]

print("Initial list:", my_list)

#Indexing
print("element at index 0:", my_list[0])

#changing an element
my_list[1]=20
print("list after changing elememt at index1:",my_list)

#append()
my_list.append(4)
print("list after appending:",my_list)

#extend()
my_list.extend([5,6])
print("list after extending:", my_list)

#insert()
my_list.insert(1,'a')
print("list after inserting 'a' at index 1:",my_list)

#remove()
my_list.remove('a')
print("list after removing 'a':",my_list)

#copy()
my_copy_list = my_list.copy()
print(my_copy_list)

#clear()
my_list.clear()
print("initial list:",my_list)
print(my_copy_list)

#index
#print("index of 3 in the :",my_list.index())

my_copy_list.sort()
my_copy_list.reverse()
print(my_copy_list)

print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])

print(len(my_copy_list))

my_list = my_copy_list.copy()
print(my_list.remove(4))