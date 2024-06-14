
import unittest
from models.expense import Expense

class TestExpense(unittest.TestCase):
    def test_expense_creation(self):
        amount = 100.0
        category = "Food"
        date = "2024-06-12"
        expense = Expense(amount, category, date)
        self.assertEqual(expense.amount, amount)
        self.assertEqual(expense.category, category)
        self.assertEqual(expense.date, date)

    def test_str_representation(self):
        amount = 100.0
        category = "Food"
        date = "2024-06-12"
        expense = Expense(amount, category, date)
        expected_str = f"Amount: ${amount}, Category: {category}, Date: {date}"
        self.assertEqual(str(expense), expected_str)

if __name__ == '__main__':
    unittest.main()
