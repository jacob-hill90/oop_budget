from modules.budget import Budget
from modules.month import Month
from modules.transaction import Transaction
from modules.category import Category

class Interface:
    def __init__(self):
        self.budget = Budget()

    def run(self):
        while True:
            self.print_menu()
            print('')
            option = int(input('Select option: '))
            if option == 1:
                month = int(input('Enter a Month (1-12): '))
                
                try:
                    cost = self.budget.get_monthly_cost(month)
                    print(f'\nYou spent ${cost} in the month of {Month(month).name}')
                except:
                    print('Error getting costs :(')

            elif option == 2:
                month = int(input('Enter month: '))
                print('')

                category_pct_costs = self.budget.get_month_costs_per_category(month)
                for cat in category_pct_costs:
                    print(f'{Category(cat).name}: {category_pct_costs[cat]} of all expenses in {Month(month).name}')

            elif option == 3:
                amount = int(input('Enter amount spent: '))
                category = int(input('Enter category: '))
                month = int(input('Enter month: '))
                txn = Transaction(amount, category, month)

                try:
                    self.budget.add_transaction(txn)
                except:
                    print('Error adding transaction :(')
                else:
                    print('\nTransaction added')
            
            elif option == 4:
                income = int(input('Enter monthly income: '))
                self.budget.set_monthly_income(income)

            elif option == 5:
                break

    def print_menu(self):
        print("\n1. See Total Monthly Expenses")
        print("2. See How You Spend")
        print("3. Add Transactions")
        print("4. Set Monthly Income")
        print("5. Quit")
