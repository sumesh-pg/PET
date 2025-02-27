from datetime import datetime
from enum import Enum, auto

# Constants
SCREEN_WIDTH = 100
EXPENSE_FILE_NAME = "data/expenses.txt"
LOG_FILE_NAME = "logs/logs.txt"
BUDGET_FILE_NAME = "data/budget.txt"

# Enum for log types
class Logtype(Enum):
    WARNING = auto()
    ERROR = auto()
    INFORMATION = auto()


# Function to write messages to log file
def log_data(logdata : str, logtype : Logtype):
    try:
        with open(LOG_FILE_NAME, "a") as file:
            file.write(str(datetime.now()) + ": " + logtype.name + ": " + logdata + "\n")
    except Exception as e:
        print(f"Unable to write to log file {e}")

# Function to check valid date format (YYYY-MM-DD)
def is_valid_date(input_date: str) -> bool:
    try:
        datetime.strptime(input_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Function to check valid amount
def is_valid_amount(input_amount: str) -> bool:
    try:
        value = float(input_amount)
        return value > 0
    except ValueError:
        return False


# Function to print a border line
def print_border():
    print("=" * SCREEN_WIDTH + "\n")

# Function to print header
def print_header(totalexpenses, budget):
    print_border()
    print("PET - Personal Expense Tracker".center(SCREEN_WIDTH) + "\n")
    print(f"Total Expenses = {totalexpenses:.2f}:  Budget = {budget:.2f}: Remaining amount to spend = {(budget - totalexpenses):.2f}".center(SCREEN_WIDTH)+ "\n")
    print_border()

# Function to display menu and get user choice
def get_menu_choice() -> str:
    print("\t 1 - Add Expense \n")
    print("\t 2 - View Expenses \n")
    print("\t 3 - Track Budget \n")
    print("\t 4 - Save Expenses \n")
    print("\t 5 - Exit \n")
    print_border()

    return input("Enter your menu choice: ").strip()

# Function to load expenses from a file
def load_expenses(file_name: str) -> tuple[list, float]:
    expenses = []
    total = 0.00
    try:
        with open(file_name, "r") as file:
            line_number = 0
            for line in file:
                line_number += 1
                # split the comma separated file
                data = line.strip().split(",")

                # remove any trailing or leading spaces in the data
                data = list(map(lambda x: x.strip(), data))

                if len(data) == 4 and is_valid_date(data[0]) and data[1] != "" and is_valid_amount(data[2]) and data[3] != "":
                    expenses.append({
                        "Date": data[0],
                        "Category": data[1],
                        "Amount": data[2],
                        "Description": data[3]
                    })

                    total += float(data[2])

                else:
                    log_data(f"Invalid data in file '{file_name}', Line number {line_number} : {line.strip()}", Logtype.ERROR)
    except FileNotFoundError:
        log_data(f"File not found - {file_name}", Logtype.WARNING)
    except Exception as e:
        log_data(f"Unknown error occurred: {e}", Logtype.ERROR)

    return expenses, total

# Function to add an expense 
def add_expense() -> dict:
    print_border()
    print("PET - Add Expense".center(SCREEN_WIDTH))
    print_border()

    try:
        while True:
            date = input("Enter date (YYYY-MM-DD): ").strip()
            if is_valid_date(date):
                break
            print("Invalid date format. Please try again.")

        while True:
            category = input("Enter category (e.g., Food, Travel): ").strip()
            if category != "":
                break
            print("Category cannot be empty. Please try again.")

        while True:
            amount = input("Enter amount: ").strip()
            if is_valid_amount(amount):
                break
            print("Invalid amount. Please try again.")

        while True:
            description = input("Enter description: ").strip()
            if description != "":
                break
            print("Desciption cannot be empty. Please try again.")

        # Create and return the expense dictionary
        expense = {
            "Date": date,
            "Category": category,
            "Amount": amount,
            "Description": description
        }
    except Exception as e:
        log_data(f"Unknown error occurred while adding expense : {e}  ")

    return expense      

# Function to conver expense as string
def get_expense_string(expense : dict) -> str:
    return expense["Date"] + "," + expense["Category"] + "," + expense["Amount"] + "," + expense["Description"] + "\n"

# Function to view all expenses
def view_expenses(expenses : list):
    print_border()
    print("\n" + "Date" + "," + "Category" + "," + "Amount" + "," + "Description" + "\n")
    print_border()
    expense_count = 0
    for expense in expenses:
        print(get_expense_string(expense))
        expense_count +=1

    print_border()
    print(f"Number of expense items : {expense_count}")
    print_border()

# Function to save all expenses to text file
def save_expenses(expenses : list, file_name : str):
    try:
        with open(file_name, "w") as file:
            for expense in expenses:
                file.write(get_expense_string(expense))

    except Exception as e:
        log_data(f"Unknown error in saving expenses : {e}", Logtype.ERROR)

def load_budget(budget_file : str) -> float:
    budget = 0
    try:
        with open(budget_file, "r") as file:
            try:
                budget = float(file.read())
            except Exception as e:
                log_data("Budget file contains invalid data", Logtype.ERROR)

    except FileNotFoundError:
        log_data(f"Budget file not found : {budget_file}", Logtype.WARNING)
    except Exception as e:
        log_data(f"Error while reading Budget file : {budget_file}", Logtype.ERROR)

    return budget

# Function to load expenses list, totalexpense and budget 
def load_data(expense_file : str, budget_file : str) -> tuple[list, float, float]:
    expenses, totalexpenses = load_expenses(expense_file)
    budget = load_budget(budget_file)
    return expenses, totalexpenses, budget

# Enum for Menu choices
class MENU_CHOICE(Enum):
    ADD_EXPENSE = "1"
    VIEW_EXPENSE = "2"
    TRACK_BUDGET = "3"
    SAVE_EXPENSE = "4"
    EXIT = "5"

# Function to compare budget with expense
def compare_budget(budget : float, expense_amount : float) :
    if expense_amount > budget:
        print(f"\nYou have exceeded your budget by {(expense_amount - budget):.2f}")
    else:
        print(f"\nYou have {(budget - expense_amount):.2f} left from the budget")

def save_budget(budget: float, budget_file: str):
    try:
        with open(budget_file, "w") as file:
            file.write("{:.2f}".format(budget))
        log_data("Budget is written to file", Logtype.INFORMATION)
    except Exception as e:
        log_data(f"Unknown error occurred while saving budget : {e}", Logtype.ERROR)

# Function to track budget
def track_budget(budget : float, expense_amount : float, budget_file : str) -> float:
    while True:
        print(f"\nCurrent Budget amount is {budget}. ")
        budget_str = input("Enter new budget amount : ") or str(budget)
        if is_valid_amount(budget_str):
            budget = float(budget_str)
            break
        else:
            print("\nInvalid amount. Please try again.")
    compare_budget(budget, expense_amount)
    save_budget(budget, budget_file)
    return budget

# Main function to run the menu in a loop
def main():

    try:
        # Load the expenses initially if the file exist
        expenses, totalexpenses, budget = load_data(EXPENSE_FILE_NAME, BUDGET_FILE_NAME)
        expenses_to_save = False

        while True:
            print_header(totalexpenses, budget)
            menu_choice = get_menu_choice()

            match menu_choice:
                case MENU_CHOICE.ADD_EXPENSE.value: 

                    expense = add_expense()
                    expenses.append(expense)
                    totalexpenses += float(expense["Amount"])
                    expenses_to_save = True
                    print("\nExpense added to the list : ", expense)
                    input("Press Enter to continue....")

                case MENU_CHOICE.VIEW_EXPENSE.value:

                    view_expenses(expenses)
                    input("Press Enter to continue....")

                case MENU_CHOICE.TRACK_BUDGET.value:
                    print_border()
                    budget = track_budget(budget, totalexpenses, BUDGET_FILE_NAME)
                    print_border()
                    input("\nPress Enter to contunue....")

                case MENU_CHOICE.SAVE_EXPENSE.value:

                    save_expenses(expenses, EXPENSE_FILE_NAME)
                    expenses_to_save = False 
                    print(f"\nExpenses saved to file {EXPENSE_FILE_NAME}")
                    input("Press Enter to continue....")

                case MENU_CHOICE.EXIT.value:

                    if expenses_to_save :
                        save_expenses(expenses, EXPENSE_FILE_NAME)

                    print_border()
                    print("\nThank you for using PET. Visit again!!!\n")
                    print_border()
                    break

                case _:
                    print("\nInvalid choice. Please try again.\n")
    except Exception as e:
        print(f"Unknown error occurred : {e}")

# Run the program - This ensures main() is called only when this file is executed directly and not when the file is imported in another file
if __name__ == "__main__":
    main()
