import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)

def add_expense(amount, category, note=""):
    expenses = load_expenses()
    expenses.append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "amount": round(float(amount), 2),
        "category": category.strip().title(),
        "note": note.strip()
    })
    save_expenses(expenses)
    print("Expense saved.")

def show_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    by_category = {}
    total = 0.0

    for item in expenses:
        amt = item["amount"]
        cat = item["category"]
        total += amt
        by_category[cat] = by_category.get(cat, 0.0) + amt

    print("\n=== Expense Summary ===")
    for cat, amt in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:<15} : {amt:.2f}")
    print("-" * 32)
    print(f"  {'Total':<15} : {total:.2f}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Expense  2. View Summary  3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                amt = float(input("Amount: "))
                cat = input("Category (e.g., Food, Travel, Bills): ")
                note = input("Note (optional): ")
                add_expense(amt, cat, note)
            except ValueError:
                print("Please enter a valid number for amount.")
        elif choice == "2":
            show_summary()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
