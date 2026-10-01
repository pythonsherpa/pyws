class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Bank account of {self.owner}"

    def __int__(self):
        return self.balance

    def __gt__(self, other):
        return self.balance > other.balance


account_john = BankAccount("John", 50)
account_jane = BankAccount("Jane", 100)
print(str(account_john))
print(int(account_john))
