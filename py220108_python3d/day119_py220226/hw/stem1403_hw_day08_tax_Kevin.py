"""
[Homework]
Date: 2022-02-26
Due date: 2022-03-04
1. Programming practice
Problem:	Set Canadian taxes for your online store
Consider a scenario that Peter, Mary, Jack want to open online stores in Canada.
Peter chooses the consumers from BC.
Mary chooses the consumers from QC.
Jack chooses the consumers from ON.
Tax Rate:
BC	GST+PST  5% + 7%
QC	GST+QST  5% + 9.975%
ON	HST            13%
Requirements:
You are asked to write a program to provide tax calculating functionalities.
Implement your design or idea by writing code
Find out entities (for classes)
Find out methods required to this business
Test code is required
Hints:
Naming convention
stem1403_hw_day08_tax_yourname.py
"""


class Address:
    def __init__(self, province):
        self.province = province


class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class OrderItem:
    def __init__(self, item_name, unit_price):
        self.item_name = item_name
        self.unit_price = unit_price


class Order:
    LAST_ORDER_NUMBER = 202112260001

    @staticmethod
    def get_next_order_no():
        Order.LAST_ORDER_NUMBER += 1

    def __init__(self, customer):
        self.items = []
        self.customer = customer

    def add_item(self, new_item):
        self.items.append(new_item)

    def remove_item(self, removed_item):
        self.items.remove(removed_item)


class OnlineStore:
    def __init__(self, customer):
        self.order1 = Order(customer)

    def calculate_pricing(self):
        price = 0
        for i in self.order1.items:
            price += i.unit_price
        return price

    def checkout(self):
        print(f"checkout(), your total is {self.calculate_pricing()}, after tax")


class BcStore(OnlineStore):
    tax_rate = 1.12  # GST + PST

    def calculate_pricing(self):
        price = 0
        for i in self.order1.items:
            price += i.unit_price
        return price * self.tax_rate


class QcStore(OnlineStore):
    tax_rate = 1.14975  # GST + QST

    def calculate_pricing(self):
        price = 0
        for i in self.order1.items:
            price += i.unit_price
        return price * self.tax_rate


class OnStore(OnlineStore):
    tax_rate = 1.13  # HST

    def calculate_pricing(self):
        price = 0
        for i in self.order1.items:
            price += i.unit_price
        return price * self.tax_rate


# test code
johns_address = Address("ON")
john = Customer("John", johns_address)
if john.address.province == "BC":
    store = BcStore(john)
elif john.address.province == "QC":
    store = QcStore(john)
elif john.address.province == "ON":
    store = OnStore(john)

iphone13 = OrderItem("iphone 13", 1099)
airpods_pro = OrderItem("airpods pro", 329)
store.order1.add_item(iphone13)
store.order1.add_item(airpods_pro)
store.checkout()
