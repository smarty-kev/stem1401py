"""
bank service
"""

import bankdata


class BankService:
    def __init__(self):
        self.bankData = bankdata.bank_data

    def __queryInterestRate(self, bankObj):
        return bankObj.getInterestRate()

    def __queryAllInterestRate(self, bankObjList):
        pass

    def __getInstanceByBankNo(self, bankNo):
        # bankData is a dictionary
        return self.bankData[bankNo]

    def __getInstances(self, bankNoList=[]):
        if len(bankNoList) == 0:
            bankNoList = list(self.bankData)

        bankObjList = []
        for bankNo in bankNoList:
            bankObjList.append(self.__getInstanceByBankNo(bankNo))
        return bankObjList

    """
    public business methods
    """

    def showInterestRate(self, bankNo):
        # see interest rate of a single bank
        if bankNo in list(self.bankData):
            bankObj = self.__getInstanceByBankNo(bankNo)
            bankName = bankObj.getBankName()
            interestRate = self.__queryInterestRate(bankObj)
            print(f'Current Interest Rate of {bankName} = {interestRate:.3%}\n')
        else:
            print("[ERROR] Invalid bank no.")

    def showInterestRateList(self):
        # see all interest rates
        bankObjects = self.__getInstances()
        print("=== Interest Rates")
        for bankObj in bankObjects:
            print(f'{bankObj.getBankName()} : {bankObj.getInterestRate():.3%}')
