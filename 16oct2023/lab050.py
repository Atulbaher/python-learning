# home work
# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
#
#
#
# input- score - 89
# output- B
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
#
# If, elif, else

A = 90-100
B = 80-89
C = 70-79
D = 60-69
F = 0-59

scale = int(input("your number\n"))

if scale >=90 and scale <= 100:
    print("grade is A")
elif scale >=80 and scale <=89:
    print("grade is B")
elif scale >=70 and scale <= 79:
    print("grade is C")
elif scale >=60 and scale <= 69:
    print("grade is D")
elif scale >=0 and scale <= 59:
    print("grade is F")
else:
    print(" invalide input")
