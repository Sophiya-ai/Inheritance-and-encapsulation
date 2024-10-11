class Test():
    def __init__(self):
        self.public = "public attribute"
        self._prot = "protected attribute"
        self.__priv = "private attribute"

    def get_private(self):
        return self.__priv

    def set_private(self, value):
        self.__priv = value


test = Test()
print(test.public)
print(test._prot)
print(test.get_private())
test.set_private("we've got private")
print(test.get_private())