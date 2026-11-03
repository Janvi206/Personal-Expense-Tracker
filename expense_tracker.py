import os
import pandas as pd
from datetime import datetime

FILE_NAME = "expenses.csv"
COLUMNS = ["Date", "Category", "Description", "Amount"]


def initialize_csv():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(FILE_NAME, index=False)


def get_total_records():
    if not os.path.exists(FILE_NAME):
        return 0
    try:
        df = pd.read_csv(FILE_NAME)
        return len(df)
    except Exception:
        return 0


def add_expense():
    print("\n--- Add Expense ---")
    raw_date = input("Enter Date (YYYY-MM-DD): ").strip()
    
    try:
        datetime.strptime(raw_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Expected format: YYYY-MM-DD. Expense not saved.")
        return

    category = input("Enter Category (e.g., Food, Travel): ").strip()
    description = input("Enter Description: ").strip()
    raw_amount = input("Enter Amount: ").strip()

    try:
        amount = float(raw_amount)
        if amount <= 0:
            print("Invalid amount. Amount must be a positive number. Expense not saved.")
            return
    except ValueError:
        print("Invalid amount. Amount must be a positive number. Expense not saved.")
        return

    new_record = pd.DataFrame([{
        "Date": raw_date,
        "Category": category,
        "Description": description,
        "Amount": amount
    }])

    new_record.to_csv(FILE_NAME, mode="a", header=not os.path.exists(FILE_NAME), index=False)
    
    total_count = get_total_records()
    print(f"Expense saved. Total records: {total_count}")


def category_summary():
    print("\n--- Category-wise Summary ---")
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return

    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses recorded yet.")
        return

    summary = df.groupby("Category")["Amount"].sum()
    total_spent = df["Amount"].sum()

    summary_str = " | ".join([f"{cat}: {int(val) if val.is_integer() else val}" for cat, val in summary.items()])
    print(summary_str)
    print(f"Total: {int(total_spent) if total_spent.is_integer() else total_spent}")


def view_all_expenses():
    print("\n--- All Recorded Expenses ---")
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No records found.")
    else:
        print(df.to_string(index=False))


def main():
    initialize_csv()
    while True:
        print("\n==============================")
        print("   PERSONAL EXPENSE TRACKER   ")
        print("==============================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category Summary")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice, please select between 1 and 4.")


if __name__ == "__main__":
    main()