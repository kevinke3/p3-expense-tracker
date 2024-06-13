# models/expense.py
import sqlite3

class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return f"Amount: ${self.amount}, Category: {self.category}, Date: {self.date}"

class ExpenseDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             amount REAL, 
                             category TEXT, 
                             date TEXT)''')
        self.conn.commit()

    def add_expense(self, expense):
        self.cursor.execute("INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)", 
                            (expense.amount, expense.category, expense.date))
        self.conn.commit()

    def get_all_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        return self.cursor.fetchall()

    def delete_expense(self, category):
        self.cursor.execute("DELETE FROM expenses WHERE category=?", (category,))
        self.conn.commit()

    def close(self):
        self.conn.close()
