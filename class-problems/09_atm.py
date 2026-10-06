# Problem Statement:
# Design an ATM class that allows a user to:
# a) Check balance
# b) Deposit money
# c) Withdraw money
# d) Display account details
# Create an object of the class and implement the operations through a menu-driven program.

class ATM:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        print("Current Balance: Rs.", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")

    def display_account_details(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance: Rs.", self.balance)


atm = ATM("Rahul", 12345, 10000)

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == 4:
        atm.display_account_details()
    elif choice == 5:
        print("Thank you for using ATM.")
        break
    else:
        print("Invalid choice.")
