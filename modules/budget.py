from modules.category import Category

class Budget:
    def __init__(self):
        self.income = 0
        self.transactions = []

    def set_monthly_income(self, income):
        self.income = income

    def get_monthly_cost(self, month):
        monthly_cost = 0
        for txn in self.transactions:
            if txn.month == month:
                monthly_cost += txn.amount
        return monthly_cost
    
    def get_month_costs_per_category(self, month):
        category_costs = {}
        for cat in Category:
            category_costs[cat.value] = 0
        
        for txn in self.transactions:
            if txn.month == month:
                category_costs[txn.category] += txn.amount
        return category_costs

    def add_transaction(self, txn):
        monthly_cost = self.get_monthly_cost(txn.month)
        if monthly_cost + txn.amount > self.income:
            print('\nYou do not have enough money!')
            raise('error')
        self.transactions.append(txn)

    def percent_report(self, month):
        total_cost = self.get_monthly_cost(month)
        category_costs = self.get_month_costs_per_category(month)
        category_pct_cost = {}
        for cat in category_costs:
            category_pct_cost[cat] = 100.0 * (category_costs[cat] / total_cost)
        return category_pct_cost
