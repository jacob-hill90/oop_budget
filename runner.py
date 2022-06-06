from modules.budget import Budget
class Interface:

    def __init__(self):
        self.budget = Budget()

    def run(self):
        while True:
            self.print_menu()
            option = int(input('Select option: '))
            if option == 1:
                pass
            elif option == 2:
                monthly_income = int(input('Enter Monthly Income: '))
            elif option == 5:
                break


    def print_menu(self):
        print("1. See Total Monthly Expenses")
        print("2. See Costs by Category")
        print("3. Add Transactions")
        print("4. Set Monthly Income")
        print("5. Quit")


#Budget review youtube 51:16 / 1:46:43