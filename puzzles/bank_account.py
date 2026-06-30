# Concept: writing a class from scratch - __init__ stores data on self; methods take an amount parameter and read/write self.balance
class Bankaccount:
    def __init__(self, balance):
        self.balance = balance
    def show(self):
        return self.balance
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        self.balance = self.balance - amount
    
b = Bankaccount(1000)
b.deposit(459)
b.withdraw(100)
print(b.show())
