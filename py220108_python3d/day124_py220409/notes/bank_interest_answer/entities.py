"""
bank provided entities
"""


class Bank:
    def __init__(self, interest_rate=None, name="Bank"):
        self.__interest_rate = interest_rate
        self.__name = name

    def getInterestRate(self):
        return self.__interest_rate

    def getBankName(self):
        return self.__name


class BankA(Bank):
    def __init__(self, interest_rate=0, name="BankA"):
        super().__init__(interest_rate, name)


class BankB(Bank):
    def __init__(self, interest_rate=0, name="BankA"):
        super().__init__(interest_rate, name)


class BankC(Bank):
    def __init__(self, interest_rate=0, name="BankA"):
        super().__init__(interest_rate, name)
