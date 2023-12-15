number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# num%2 == 0
# even_number = [2,4,6,8,10]

# filter -> number element can be less or equal the list

def is_even(num):
    return num % 2 == 0


# mod
# 2|10|5
# 10
# -----
# 0


even_number = filter(is_even, number)
print(even_number)
even_number_list = list(even_number)
print(even_number_list)