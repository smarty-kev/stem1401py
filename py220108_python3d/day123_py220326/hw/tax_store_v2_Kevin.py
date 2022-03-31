"""
v2 calculate tax for different online stores in different provinces of Canada
"""


class TaxRate:
    def __init__(self, tax_rate=None):
        self.tax_rate = tax_rate

    def getTax(self):
        return self.tax_rate


class GST(TaxRate):
    def __init__(self, tax_rate=0.05):
        self.tax_rate = tax_rate


class HST(TaxRate):
    def __init__(self, tax_rate=0.15):
        self.tax_rate = tax_rate


class PST(TaxRate):
    def __init__(self, tax_rate=None):
        self.tax_rate = tax_rate


class OrderItem:
    def __init__(self, unit_price):
        self.unit_price = unit_price


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, new_item):
        self.items.append(new_item)


class OnlineStore:
    def __init__(self, tax_rate):
        self.order = Order()
        self.tax_rate = tax_rate

    def calculate_pricing(self):
        price = 0
        for i in self.order1.items:
            price += i.unit_price
        return price * (1+self.tax_rate)

    def checkout(self):
        print(f"checkout(), your total is {self.calculate_pricing()}, after tax")


# main program
# tax rates for every canadian province
alberta = GST().tax_rate
british_columbia = GST().tax_rate + PST(0.07).tax_rate
manitoba = GST().tax_rate + PST(0.08).tax_rate
new_brunswick = HST().tax_rate
newfoundland = HST().tax_rate  # and labrador
northwest_territories = GST().tax_rate
nova_scotia = HST().tax_rate
nunavut = GST().tax_rate
ontario = GST().tax_rate + HST(0.08).tax_rate
prince_edward_island = HST().tax_rate
quebec = GST().tax_rate + PST(0.09975).tax_rate
saskatchewan = GST().tax_rate + PST(0.06).tax_rate
yukon = GST().tax_rate


peter_store = OnlineStore(british_columbia)
mary_store = OnlineStore(quebec)
jack_store = OnlineStore(ontario)
