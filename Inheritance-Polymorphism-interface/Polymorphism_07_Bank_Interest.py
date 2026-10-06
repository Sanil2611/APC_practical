# Problem Statement:
# Create a base class BankAccount with a method calculate_interest(). Derive SavingsAccount,
# CurrentAccount, and FixedDepositAccount. Override the method to calculate interest differently
# for each account type.

class BankAccount:
    def calculate_interest(self, balance):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.06


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.02


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.08


accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]

for account in accounts:
    print("Interest:", account.calculate_interest(50000))
