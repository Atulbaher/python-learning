my_dict = {'a':1, 'b':2}
val = my_dict.pop('a')
print(val)
print(my_dict)

# Api testing -> JSON so we can use Dict which ic similiar data type as JSON

print(dir(dict))

#how to itterate over the Dict ?

knights = {'gallahad': 'the pure', 'robin':'the brave'}
print(len(knights))

for k,v in knights.items():
    print(k,v)
    