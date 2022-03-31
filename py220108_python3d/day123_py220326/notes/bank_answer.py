"""

"""


class Bank:
    def __init__(self, interest_rate=None):
        self.interest_rate = interest_rate

    def getInterestRate(self):
        return self.interest_rate


class BankA(Bank):
    def getInterestRate(self):
        return self.interest_rate


class BankB(Bank):
    def getInterestRate(self):
        return self.interest_rate


class BankC(Bank):
    def getInterestRate(self):
        return self.interest_rate


class InterestInfoApp:
    def queryInterestRate(self, bankObj):
        result = bankObj.getInterestRate()
        return result

    def queryMultiInterestRate(self, *bankObj):
        multiInterestRate = []
        for bank in bankObj:
            multiInterestRate.append(bank.getInterestRate())
        return multiInterestRate


# main
bank1 = BankA(0.04)
bank2 = BankB(0.0395)
bank3 = BankC(0.035)

myapp = InterestInfoApp()
