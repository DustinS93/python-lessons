# Concept: defining a class with __init__ and a methond that uses self

class Expense:
    def __init__(self, desc, category, amount):
        self.desc = desc
        self.category = category
        self.amount = amount
    def summary(self):
        return f"{self.desc} - {self.category} - {self.amount:.2f}"

e = Expense("Coffee", "Food", 3.33)
e2 = Expense("Puppies", "Dogs", 99.99)
print(e.summary())
print(e2.summary())