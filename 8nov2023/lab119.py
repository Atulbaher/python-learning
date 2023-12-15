class Passeord:
    def __init__(self,password):
        self.__password = password
        self.public_var = password

    def get_password(self,is_auth):
        if is_auth:
            return self.__password
        else:
            print("Error")

    def set_pasword(self,password):
        if len(password)>10:
            self.__password = password
        else:
            print("week password")

    def print_len(self):
        print("your password len is",len(self.__password))


pwd = Passeord("haker123")
pwd.public_var
pwd.print_len()
pssd = pwd.get_password(False)
print(pssd)

#pwd.__psddword

pwd.set_pasword("Atul123123")
pwd.print_len()