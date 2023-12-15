tuple3 = tuple(["atul","baher"])
print(tuple3)
print(tuple3[0])
print(tuple3[1])

# Merging Tuples

hero1 = ("batman","bruce wayne")
hero2 = ("wonder woman","diana prince")
awesome_team = (hero1,hero2)
print(awesome_team)

#convert to list

my_tuple =(1,2,3,4,5)
print(list(my_tuple))

x =10
a,b =23,24 # this is multiple value assing
q,w,e = (45,56,78) # tuple is assing to multiple variables
print(q)
print(w)
print(e)

#Nested tuples

hero1 = ("batman","bruce wayne")
hero2 = ("wonder woman","diana prince")
awesome_team = (hero1,hero2)
print(len(awesome_team))
print(awesome_team[0])
print(awesome_team[1])

print(awesome_team[0][1])
print(awesome_team[1][1])

#Search in tuple
cities = ("london","paris","l0s vagas","tokyo")
print("paris" in cities)
print("moscow" in cities)