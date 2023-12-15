t = ("the testing academy", "for", "the testing academy")
print("\n set with the use of tuple:")
print(set(t))
set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.intersection(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set1 = set1.difference(set2)
my_set2 = set2.difference(set1)
print(my_set1)
print(my_set2)

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
subset = set2.issubset(set1)
print(subset)

# 11 =[1,2,3,4,5]
# 12 =[1,2,3,4,5]
# 13 =11

set1 = set(["the testing academy", "for", "the testing academy."])
print(set1)

for i in set1:
    print(i)
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
set1.remove(5)
set1.remove(6)
print(set1)
