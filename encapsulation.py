class AccountHolder:
    def __init__(self):
        self.__accountNumber = 12345
        self.__balance = 3456
        self.__password = 123

    def setPassword(self, p):
        self.__password = p

    def getPassword(self):
        return self.__password

    def getBalance(self):
        return self.__balance


a = AccountHolder()
print(a.getBalance())
