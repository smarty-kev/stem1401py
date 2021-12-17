"""
Boxing Day Project : v1
Author : Kevin Liu
Started : 11 December 2021
Last modified : 17 December 2021
"""

import datetime


class Address:
    def __init__(self, street_number, street, city, province, country, postal_code):
        self.street_number = street_number
        self.street = street
        self.city = city
        self.province = province
        self.country = country
        self.postal_code = postal_code
        self.address = f"{self.street_number} {self.street} {self.city}, {self.province} {self.country} {self.postal_code}"


class Customer:
    def __init__(self, billing_name, billing_address, receiver_name, shipping_address):
        self.billing_name = billing_name
        self.billing_address = billing_address
        self.receiver_name = receiver_name
        self.shipping_address = shipping_address


class OrderItem:
    def __init__(self,item_number, item_name, item_description, unit_price, item_quantity=1):
        self.item_number = item_number
        self.item_name = item_name
        self.item_description = item_description
        self.unit_price = unit_price
        self.item_quantity = item_quantity
        self.amount = float(unit_price) * item_quantity


class Status:
    SHIPMENT_SHIPPED = "shipped"
    SHIPMENT_READY = "ready to ship"
    SHIPMENT_NOT_READY = "not ready to ship"
    ORDER_PAID = "order is paid"
    ORDER_UNPAID = "order is not paid"
    ORDER_CANCELLED = "order is cancelled"


class TaxRate:
    # taxes in Quebec
    GST = 0.05
    QST = 0.09975


class Order:
    LAST_ORDER_NUMBER = 202112260001

    @staticmethod
    def get_next_order_no():
        Order.LAST_ORDER_NUMBER += 1

    def __init__(self, customer, date=datetime.datetime.now().strftime("%m-%d-%Y"), time=datetime.datetime.now().strftime("%X")):
        self.items = []
        self.customer = customer
        self.date = date
        self.time = time
        self.shipment_status = Status.SHIPMENT_NOT_READY
        self.order_status = Status.ORDER_UNPAID

    def add_item(self, new_item):
        self.items.append(new_item)

    def remove_item(self, removed_item):
        self.items.remove(removed_item)

    def confirm_order(self):
        # informs the merchant that the customer wants to buy the items
        self.shipment_status = Status.SHIPMENT_READY

    def pay_bill(self):
        self.order_status = Status.ORDER_PAID
        # informs merchant of order info
        # merchant ships the ordered items
        self.shipment_status = Status.SHIPMENT_SHIPPED

    def cancel_order(self):
        if self.order_status != Status.ORDER_PAID:  # only if the user hasn't paid
            self.order_status = Status.ORDER_CANCELLED
            # informs merchant of cancellation
            self.shipment_status = Status.SHIPMENT_NOT_READY

    def __str__(self):
        items_info = []
        index = 1
        for i in self.items:
            items_info.append(index)
            items_info.append(i.item_number)
            items_info.append(i.item_name)
            items_info.append(i.item_description)
            items_info.append(i.unit_price)
            items_info.append(i.item_quantity)
            items_info.append(i.amount)
            index += 1

        order_info = f"================\n" \
                     f"ABC.ca     ORDER\n" \
                     f"================\n" \
                     f"Order no. :    {self.LAST_ORDER_NUMBER}\n" \
                     f"Order date:    {self.date}\n" \
                     f"Order time:    {self.time}\n" \
                     f"Bill To: {self.customer.billing_name}\n" \
                     f"         {self.customer.billing_address.address}\n" \
                     f"Ship TO: {self.customer.receiver_name}\n" \
                     f"         {self.customer.shipping_address.address}\n" \
                     f"================\n"

        count = 0  # there are 7 info for each item
        for info in items_info:
            count += 1
            order_info += str(info) + " "
            if count % 7 == 0:
                order_info += "\n"  # to switch line
        order_info += "================\n"

        # bill info
        subtotal = 0
        for item in self.items:
            subtotal += float(item.amount)

        if subtotal > 50:
            freight = 0
        else:
            freight = 25

        tax_gst = subtotal * TaxRate.GST
        tax_qst = subtotal * TaxRate.QST

        total = subtotal + freight + tax_qst + tax_gst

        # bill template
        bill_info = f"Subtotal:     {subtotal}\n" \
                    f"Freight:      {freight}\n" \
                    f"GST @5.000%:  {tax_gst}\n" \
                    f"QST @9.975%   {tax_gst}\n" \
                    f"Total         {total}\n"   \
                    f"================\n" \
                    f"Status: {self.order_status}, {self.shipment_status}"
        order_info += bill_info

        return order_info


# main program
peter_address = Address("9-1000", "Boul. Decarie", "Montreal", "Quebec", "Canada", "H2A 1K3")
customer1 = Customer("Peter", peter_address, "Peter", peter_address)
order1 = Order(customer1, "12-26-2021", "20:00:00")

iphone = OrderItem("101001", "iPhone 13", "64GB Black", "1200")
flash_drive = OrderItem("102005", "USB Flash Drive", "8GB", "14.99", 2)
book = OrderItem("201006", "Book", "The Art of Code", "59.99")

order1.add_item(iphone)
order1.add_item(flash_drive)
order1.add_item(book)

order1.pay_bill()
print(order1)
print("\n")  # two new lines for next order


Order.get_next_order_no()
jack_address = Address("3-1500", "Boul. Sherbrooke Est.", "Quebec City", "Quebec", "Canada", "K1B 2H6")
customer1.receiver_name = "Jack"
customer1.shipping_address = jack_address
order2 = Order(customer1, "12-26-2021", "20:30:00")

box_of_chocolate = OrderItem("401002", "Chocolate", "12 pieces 360g", "9.99")
game_disc = OrderItem("502003", "Game disc", "Call of Duty, Elder Scroll for XBox", "11.99", 2)
order2.add_item(box_of_chocolate)
order2.add_item(game_disc)

order2.pay_bill()
print(order2)
