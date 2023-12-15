class BankAccount:
    def __init__(self):
        self.balance = 0  # Instance variable(you can access it via only object)
        self.__Private_var = 100

    def deposit(self, amount):  # Public function
        # self.balance = self.balance + amount
        self.balance += amount

    def _withdraw(self, amount):  # Protected
        self.balance -= amount

    def __show_balance(self):  # private
        print("your balance", self.balance)

    def IS_Auth_True_shoe_bal(self, isAuth):
        if isAuth:
            self.__show_balance()
        else:
            print("you are not Auth")

    def do_withdraw_by_banl_manager(self, amount):
        self._withdraw(amount=amount)


jp_chase = BankAccount()
jp_chase.deposit(1000)
jp_chase._withdraw(499)  # not a good practise(Protected)



#Newer use this

jp_chase._BankAccount__private_var = 100
print(jp_chase._BankAccount__private_var) # super bad practice - python allow this


#write the code to Auth _ DEv
# jp_chase.IS_AuthTrue_show_bal(True)
jp_chase.IS_Auth_True_shoe_bal(False)