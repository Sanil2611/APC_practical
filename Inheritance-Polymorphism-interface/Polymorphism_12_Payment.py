# Problem Statement:
# Develop an online shopping payment module using polymorphism. Create a base class Payment
# and derived classes UPIPayment, CardPayment, and WalletPayment. Each class should implement
# its own make_payment() method. Demonstrate polymorphism using a common function.

class Payment:
    def make_payment(self, amount):
        pass


class UPIPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using UPI")


class CardPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using Card")


class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using Wallet")


def process_payment(payment, amount):
    payment.make_payment(amount)


payments = [UPIPayment(), CardPayment(), WalletPayment()]

for payment in payments:
    process_payment(payment, 1000)
