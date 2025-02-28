import os
from logger import log_data
from constants import LogType, PRINT_DATE_WIDTH, PRINT_AMOUNT_WIDTH, PRINT_CATEGORY_WIDTH
from utils import print_border, is_valid_date, is_valid_amount

def load_expenses(file_name: str):
    """Loads expenses from a file and calculates the total amount."""
    expenses = []
    total = 0.0

    if not os.path.exists(file_name):
        log_data(f"File not found - {file_name}", LogType.WARNING)
        return expenses, total

    with open(file_name, "r") as file:
        for line_number, line in enumerate(file, start=1):
            data = [x.strip() for x in line.strip().split(",")]

            if len(data) == 4 and is_valid_date(data[0]) and data[1] and is_valid_amount(data[2]) and data[3]:
                expenses.append({"Date": data[0], "Category": data[1], "Amount": data[2], "Description": data[3]})
                total += float(data[2])
            else:
                log_data(f"Invalid data at line {line_number} in {file_name}: {line.strip()}", LogType.ERROR)

    return expenses, total

def save_expenses(expenses: list, file_name: str):
    """Saves the expense list to a file."""
    try:
        with open(file_name, "w") as file:
            for expense in expenses:
                file.write(get_expense_string(expense))
                #file.write(f"{expense['Date'].ljust(PRINT_DATE_WIDTH)},{expense['Category'].ljust(PRINT_CATEGORY_WIDTH)},{expense['Amount'].ljust(PRINT_AMOUNT_WIDTH)},{expense['Description'].ljust(PRINT_DESCRIPTION_WIDTH)}\n")
    except Exception as e:
        log_data(f"Error saving expenses: {e}", LogType.ERROR)

def add_expense() -> dict:
    """Prompts the user to input expense details and returns an expense dictionary."""
    print_border()
    print("PET - Add Expense".center(100))
    print_border()

    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if is_valid_date(date):
            break
        print("Invalid date format. Please try again.")

    while True:
        category = input(f"Enter category (e.g., Food, Travel - max {PRINT_CATEGORY_WIDTH} characters) : ").strip()[:PRINT_CATEGORY_WIDTH]
        if category:
            break
        print("Category cannot be empty. Please try again.")

    while True:
        amount = input("Enter amount: ").strip()
        if is_valid_amount(amount):
            break
        print("Invalid amount. Please try again.")

    while True:
        description = input("Enter description: ").strip()
        if description:
            break
        print("Description cannot be empty. Please try again.")

    return {
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Description": description
    }

def view_expenses(expenses: list):
    """Displays all stored expenses."""
    print_border()
    print("DATE".ljust(PRINT_DATE_WIDTH) + "," + "CATEGORY".ljust(PRINT_CATEGORY_WIDTH) + "," + "AMOUNT".ljust(PRINT_AMOUNT_WIDTH) + "," + "DESCRIPTION")
    print_border()

    for expense in expenses:
        print(get_expense_string(expense).strip())

    print_border()
    print(f"Total Expenses: {len(expenses)} items")
    print_border()

def get_expense_string(expense: dict) -> str:
    """Formats an expense dictionary into a string for file storage or display."""
    return f"{expense['Date'].ljust(PRINT_DATE_WIDTH)},{expense['Category'].ljust(PRINT_CATEGORY_WIDTH)},{expense['Amount'].ljust(PRINT_AMOUNT_WIDTH)},{expense['Description']}\n"

