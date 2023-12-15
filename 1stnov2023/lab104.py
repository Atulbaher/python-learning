number = [1, -2, -3, -4, 5, 16, -7, 8, -9, -10]


def is_positive(num):
    return num > 0


pos_number = filter(is_positive, number)
print(pos_number)
pov_number_list = list(pos_number)
print(pov_number_list)

