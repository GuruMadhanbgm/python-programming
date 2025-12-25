class Customer:
    def __init__(self, name, pnumber, address):
        self.name = name
        self.pnumber = pnumber
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Phone Number:", self.pnumber)
        print("Address:", self.address)

    def order(self):
        print("Ordering food")

    def cancel_order(self):
        print("Cancelling food")

    def payment(self):
        print("Paying amount")


class GoldCustomer(Customer):
    def __init__(self, name, pnumber, address, gold_id):
        super().__init__(name, pnumber, address)
        self.gold_id = gold_id

    def display(self):
        super().display()
        print("Gold ID:", self.gold_id)

    def free_delivery(self):
        print("Ordering with no delivery cost")


# Main program
c = Customer("madhan", 12345, "proddatur")
g = GoldCustomer("prasad", 45678, "kadapa", 1)

print("==============")
print("Customer Details:")
c.display()

print("\n==============")
print("Gold Customer Details:")
g.display()
g.free_delivery()
