"""
Boxing Day Project : v1
Author : Kevin Liu
Started : 11 December 2021
Last modified : 11 December 2021
"""

import datetime


class Address:
    def __init__(self, street, ):
        pass


class Customer:
    def __init__(self, name, billing_address, receiver_name, shipping_address):
        self.name = name
        self.billing_address = billing_address
        self.receiver_name = receiver_name
        self.shipping_address = shipping_address


class Item:
    def __init__(self):
        pass


class Status:
    SHIPMENT_SHIPPED = "shipped"
    SHIPMENT_READY = "ready to ship"
    SHIPMENT_NOT_READy = "not ready to ship"
    ORDER_PAID = "order is paid"
    ORDER_UNPAID = "order is not paid"
    ORDER_CANCELLED = "order is cancelled"


class TaxRate:
    # taxes
    GST = 0.05
    QST = 0.09975


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, new_item):
        self.items.append(new_item)

    def remove_item(self, removed_item):
        self.items.remove(removed_item)


class Order:
    LAST_ORDER_NUMBER = 1001

    @staticmethod
    def get_next_order_no():
        Order.LAST_ORDER_NUMBER += 1
