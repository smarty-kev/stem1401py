"""
class method

project : Order System
"""


class Order:
    currentOrderID = 0

    @classmethod
    def getNextOrderID(cls):
        nextOrderID = cls.currentOrderID + 1
        cls.currentOrderID = nextOrderID
        return nextOrderID


# test
# access via class name
print(Order.getNextOrderID())

# access via instance
order1 = Order()
print(order1.getNextOrderID())

