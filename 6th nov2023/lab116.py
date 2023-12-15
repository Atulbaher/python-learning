class Myclass:

    def __int__(self):
        self.__privatr_toilate = "private toilet only atul allowed"
        self._protected_attribute = 42
        self.public_var = 55

    def __private_method(self):
        return "this is a private method"


obj = Myclass
# print(obj.__private_toilet)


# Learn about the Private, Protected and Public variables