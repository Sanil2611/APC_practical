# Problem Statement:
# Create a base class BankAccount with account number and balance. Derive SavingsAccount
# from it with an interest rate. Further derive PremiumSavingsAccount with additional benefits.
# Define methods to calculate interest and display account details.

class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)
        print("Interest:", self.calculate_interest())
        print("Benefits:", self.benefits)


p = PremiumSavingsAccount(10001, 50000, 6, "Airport Lounge Access")
p.display()
