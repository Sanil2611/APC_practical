# Problem Statement:
# Create an abstract class BankAccount with abstract methods deposit() and withdraw().
# Derive SavingsAccount and CurrentAccount and implement the required operations.

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount


class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


accounts = [SavingsAccount(10000), CurrentAccount(15000)]

for account in accounts:
    account.deposit(2000)
    account.withdraw(3000)
    print("Balance:", account.balance)
