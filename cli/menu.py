# cli/menu.py
from models.expense import Expense, ExpenseDB

class Menu:
    def __init__(self):
        self.options = {}
        self.expense_db = ExpenseDB('expenses.db')

    def add_option(self, key, description, callback):
        self.options[key] = (description, callback)

    def display(self):
        print("\nMenu:")
        for key, (description, _) in self.options.items():
            print(f"{key}: {description}")
        print("X: Quit")

    def run(self):
        while True:
            self.display()
            choice = input("Enter your choice: ").strip().lower()

            if choice == 'X':
                print("See yaaah...")
                self.expense_db.close_connection()
                break

            if choice in self.options:
                _, callback = self.options[choice]
                callback()
            else:
                print("Hell nooooo!!!!")

def add_expense_menu():
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    expense = Expense(amount, category, date)
    menu.expense_db.add_expense(expense)
    print("Successs")

def view_expenses_menu():
    expenses = menu.expense_db.get_all_expenses()
    for expense in expenses:
        print(f"Amount: ${expense[0]}, Category: {expense[1]}, Date: {expense[2]}")

def delete_expense_menu():
    category = input("Enter the category of the expense to be deleted: ")
    menu.expense_db.delete_expense(category)
    print("Dont regret.")

menu = Menu()
menu.add_option('1', 'Add Expense', add_expense_menu)
menu.add_option('2', 'View Expenses', view_expenses_menu)
menu.add_option('3', 'Delete Expense', delete_expense_menu)

if __name__ == "__main__":
    menu.run()
