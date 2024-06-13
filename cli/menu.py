from models.expense import Expense, Session
from datetime import datetime

def show_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Delete Expense")
    print("4. Exit")

def add_expense():
    session = Session()
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date_str = input("Enter date (YYYY-MM-DD): ")
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        new_expense = Expense.create(session, amount, category, date)
        print(f"Expense added: {new_expense}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    finally:
        session.close()

def view_expenses():
    session = Session()
    expenses = Expense.get_all(session)
    if expenses:
        for expense in expenses:
            print(expense)
    else:
        print("No expenses found.")
    session.close()

def delete_expense():
    session = Session()
    try:
        expense_id = int(input("Enter expense ID to delete: "))
        if Expense.delete(session, expense_id):
            print("Expense deleted successfully!")
        else:
            print("Expense not found.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    finally:
        session.close()

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")