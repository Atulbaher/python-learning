# Single inheritance - 90%
# use the properties, variable and method of your base class or parent by the sub class or son class



class Father:
    bank_bal = 100

    def one_bhk(self):
        print("use it son")


class Son(Father):
    pass # i will write the code in future !! skip


s = Son()

s.one_bhk()
print(s.bank_bal)