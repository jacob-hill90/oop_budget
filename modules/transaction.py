from modules.category import Category

class Transaction:
    def __init__(self, amount, category, month):
        self.amount = amount
        self.category = category
        self.month = month
