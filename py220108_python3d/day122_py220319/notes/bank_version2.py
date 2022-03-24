"""

"""


class Bank:
    def __init__(self, interest_rate, bank_name=None):
        self.bank_name = bank_name
        self.interest_rate = interest_rate
        self.accounts = []

    def open_account(self, new_account):
        self.accounts.append(new_account)

    def check_interest_rate(self):
        return self.interest_rate

    def change_interest_rate(self, new_interest_rate):
        self.interest_rate = new_interest_rate


class BankA(Bank):
    pass


class BankB(Bank):
    pass


class BankC(Bank):
    pass


class InterestInfoApp:
    def __init__(self, *banks):
        self.banks = banks

        self.highest_interest = None
        self.highest_interest_bank = None

        self.lowest_interest = None
        self.lowest_interest_bank = None

    def get_highest_interest(self):
        highest = 0
        highest_interest_bank = None
        for bank in self.banks:
            if bank.check_interest_rate() > highest:
                highest = bank.check_interest_rate()
                highest_interest_bank = bank.bank_name
        self.highest_interest = highest
        self.highest_interest_bank = highest_interest_bank

    def get_lowest_interest(self):
        lowest = 1
        lowest_interest_bank = None
        for bank in self.banks:
            if bank.check_interest_rate() < lowest:
                lowest = bank.check_interest_rate()
                lowest_interest_bank = bank.bank_name
        self.lowest_interest = lowest
        self.lowest_interest_bank = lowest_interest_bank

    def get_interests_info(self):
        info = ""
        for i in range(len(self.banks)):
            info += self.banks[i].bank_name
            info += " = "
            info += str(self.banks[i].check_interest_rate())
            info += "\n"

        self.get_highest_interest()
        info += f"Highest Interest = {self.highest_interest}, {self.highest_interest_bank}"

        info += "\n"

        self.get_lowest_interest()
        info += f"Lowest Interest = {self.lowest_interest}, {self.lowest_interest_bank}"

        return info


BankA = Bank("BankA", 0.04)
BankB = Bank("BankB", 0.0395)
BankC = Bank("BankC", 0.035)

app = InterestInfoApp(BankA, BankB, BankC)
print(app.get_interests_info())
