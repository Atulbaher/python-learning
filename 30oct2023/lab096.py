# Dict

my_dict = {'a':1,'b':2,'c':3,"a":95}
print(my_dict)

# If you have a duplicate key' latest value of key will be used!!

keys = my_dict.keys()
values = my_dict.values()

#get all the keys in to a list

key_list = list(keys)
print(values)

print(key_list[0])
print(key_list[1])
print(key_list[2])


# Dict key and value

#my_dict.clear()
print(my_dict)
copy_my_dict = my_dict.copy()
print(copy_my_dict)

print(my_dict.items())

set_dic = set(my_dict.items())