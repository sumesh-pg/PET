from datetime import datetime
from enum import Enum, auto

# Constants
SCREEN_WIDTH = 40
DATA_FILE_NAME = "data\expenses.txt"
LOG_FILE_NAME = "logs\logs.txt"

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
def print_header():
    print_border()
    print("PET - Personal Expense Tracker".center(SCREEN_WIDTH) + "\n")
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
def load_expenses(file_name: str) -> list:
    expenses = []
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
                else:
                    log_data(f"Invalid data in file '{file_name}', Line number {line_number} : {line.strip()}", Logtype.ERROR)
    except FileNotFoundError:
        log_data(f"File not found - {file_name}", Logtype.WARNING)
    except Exception as e:
        log_data(f"Unknown error occurred: {e}", Logtype.ERROR)

    return expenses

# Function to add an expense 
def add_expense() -> dict:
    print_border()
    print("PET - Add Expense".center(SCREEN_WIDTH))
    print_border()

    # Get user inputs with validation
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
        print("Invalid amount. Please enter a valid amount.")

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
    
    return expense      

def view_expenses(expenses : list):
    for item in expenses:
        date = item["Date"]
        category = item["Category"]
        amount = item["Amount"]
        description = item["Description"]



# Main function to run the menu in a loop
def main():
    # Load the expenses initially if the file exist
    expenses = load_expenses(DATA_FILE_NAME)
    
    while True:
        print_header()
        menu_choice = get_menu_choice()

        match menu_choice:
            case "1":
                print("\nUser chose to add an expense")
                expenses.append(add_expense())
                print(expenses)
            case "2":
                print("\nUser chose to view expenses")
            case "3":
                print("\nUser chose to track budget")
            case "4":
                print("\nUser chose to save expenses")
            case "5":
                print("Thank you for using PET. Visit again!!!")
                break
            case _:
                print("\nInvalid choice. Please try again.\n")

# Run the program - This ensures main() is called only when this file is executed directly and not when the file is imported in another file
if __name__ == "__main__":
    main()
