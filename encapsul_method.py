class Test():
    def pub(self):
        print("Public method")

    def _prot(self):
        print("Protected method")

    def __priv(self):
        print("Private method")

    def test_private(self):
        self.__priv()

t = Test()
t.pub()
t._prot()
t.test_private()