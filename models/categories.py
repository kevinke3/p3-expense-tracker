# models/categories.py

class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Category: {self.name}"
