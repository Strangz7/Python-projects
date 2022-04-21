class Account:
    def __init__(self, name):
        self.balance = 0
        self.name = name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, withdraw):
        if withdraw < self.balance:
            self.balance -= withdraw

    def transfer(self, transfer, other):
        self.withdraw(transfer)
        self.deposit(other)
