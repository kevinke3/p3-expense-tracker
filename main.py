# main.py

from cli.menu import Menu
from models.expense import Expense, ExpenseDB

def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    date = input("Enter expense date (YYYY-MM-DD): ")
    expense = Expense(amount, category, date)
    expense_db.add_expense(expense)
    print("Expense added successfully!")

def view_expenses():
    expenses = expense_db.get_all_expenses()
    if not expenses:
        print("No expenses found.")
    else:
        for exp in expenses:
            print(f"ID: {exp[0]}, Amount: ${exp[1]}, Category: {exp[2]}, Date: {exp[3]}")

def delete_expense():
    category = input("Enter the category of the expense to delete: ")
    expense_db.delete_expense(category)
    print("Expense deleted successfully!")

if __name__ == "__main__":
    expense_db = ExpenseDB('expenses.db')

    menu = Menu()
    menu.add_option('a', 'Add Expense', add_expense)
    menu.add_option('v', 'View Expenses', view_expenses)
    menu.add_option('d', 'Delete Expense', delete_expense)

    menu.run()
    expense_db.close()
