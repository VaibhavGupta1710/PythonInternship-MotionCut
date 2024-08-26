import os
import json

# File to store the expenses
EXPENSES_FILE = 'expenses.json'


def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r') as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    description = input("Enter the description of the expense: ")
    amount = float(input("Enter the amount of the expense in Rs: "))
    expenses.append({'description': description, 'amount': amount})
    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    print("\nExpenses:")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['description']} - Rs{expense['amount']:.2f}")
    print()


def delete_expense(expenses):
    view_expenses(expenses)
    index = int(input("Enter the number of the expense to delete: ")) - 1
    if 0 <= index < len(expenses):
        expenses.pop(index)
        print("Expense deleted successfully!")
    else:
        print("Invalid index.")


def main():
    expenses = load_expenses()

    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter your choice(1/2/3/4): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
        elif choice == '4':
            save_expenses(expenses)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
