"""
2. Rewrite Bank Interest
"""


class Bank:
    def __init__(self, interest_rate=None, name="Bank"):
        self.interest_rate = interest_rate
        self.name = name

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
    def find_interest_rate(self, bankObj):
        return bankObj.getInterestRate()

    def find_multiple_interest_rate(self, *bankObjs):
        multiple_interest_rate = []
        for bank in bankObjs:
            multiple_interest_rate.append(bank.getInterestRate())
        return multiple_interest_rate


# main
bank1 = BankA(0.04, "Bank A")
bank2 = BankB(0.0395, "Bank B")
bank3 = BankC(0.035, "Bank C")

myapp = InterestInfoApp()
print("Bank A interest rate:")
print(myapp.find_interest_rate(bank1))

print("Bank B interest rate:")
print(myapp.find_interest_rate(bank2))

print("Bank C interest rate:")
print(myapp.find_interest_rate(bank3))
