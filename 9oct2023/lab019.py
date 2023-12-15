# string
# Bunch of Char
name = "Atul"
print(name)
name = "baher"
print(name)

# string functions
# Python string Immutable in Nature - They cant changed onec created
# # name[0] = "h" # TypeError: 'str' object does not support item assignment

# capitalize()
# return a copy of the string with its first character capitalized.
result = name.capitalize()
print(result)
print(name)
print(id(name))
print(id(name))
print(print(id(result)))

# upper case
result2 = name.upper()
print(result2)

# lower case
result3 = name.lower()
print(result3)

# swapcase()
# returns a copy of the string with uppercase characters converted to lowercase
# and vice versa

name = "AtUlBaHeR"
print(name.swapcase())

# Title
# returns a titlecased version of the string
# where words start with an uppercase charecter and
# the remaning charecter are lowercase
name = " hello india"
print(name.title())

name = "atul"
print(len(name))

# Replace
text = "hello world"
result_rep =text.replace("world","python")
print(result_rep)

name = "i love india"
resultrep = name.replace("love","like")
print(resultrep)

#find()
#Returns the lowest index of a substring in the string.
# Returns -1 if the substring is not found.

text = "hello world"
index = text.find("world")
print(index)

#count() - count the char -
count = text.count("l")
print(count)

name = "p d"
print(len(name))