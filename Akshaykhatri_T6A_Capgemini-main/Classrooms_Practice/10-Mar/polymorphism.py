class UPI:
    
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class DebitCard:
    
    def pay(self, amount):
        print("Paid", amount, "using Debit Card")


class CreditCard:
    
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


# Creating objects
u = UPI()
d = DebitCard()
c = CreditCard()

# Calling same method
u.pay(500)
d.pay(1000)
c.pay(2000)