import csv
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"

# Step 1: Initialize file with headers if not exists
try:
    with open(FILE_NAME, "x", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Note"])
except FileExistsError:
    pass  # file already exists

def add_expense():
    """Add a new expense entry"""
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food/Transport/Shopping/Others): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note (optional): ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("✅ Expense added successfully!\n")


def view_expenses():
    """Display all expenses"""
    print("\n--- All Expenses ---")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()


def summary():
    """Show total spent per category"""
    categories = {}
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cat = row["Category"]
            amt = float(row["Amount"])
            categories[cat] = categories.get(cat, 0) + amt

    print("\n--- Expense Summary ---")
    for cat, total in categories.items():
        print(f"{cat}: ₹{total:.2f}")
    
    # Optional: show pie chart
    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title("Expenses by Category")
    plt.show()


# Main Menu
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Summary")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        summary()
    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice, try again.")
