from constants import EXPENSE_FILE_NAME, BUDGET_FILE_NAME, SCREEN_WIDTH, MenuChoice
from utils import print_border
from expense_manager import load_expenses, save_expenses, add_expense, view_expenses
from budget_manager import load_budget, save_budget, compare_budget

def print_header(total_expenses, budget):
    """Prints the application header with budget details."""
    print_border()
    print("PET - Personal Expense Tracker".center(SCREEN_WIDTH) + "\n")
    print(f"Budget: {budget:.2f} | Total Expenses: {total_expenses:.2f} | {"Remaining" if budget > total_expenses else "Overspend"}: {abs((budget - total_expenses)):.2f}".center(SCREEN_WIDTH))
    print_border()

def get_menu_choice():
    """Displays menu and returns user choice."""
    print("\t 1 - Add Expense\n")
    print("\t 2 - View Expenses\n")
    print("\t 3 - Track Budget\n")
    print("\t 4 - Save Expenses\n")
    print("\t 5 - Exit\n")
    print_border()
    return input("Enter your choice: ").strip()

def main():
    """Main function to handle user interactions."""
    expenses, total_expenses = load_expenses(EXPENSE_FILE_NAME)
    budget = load_budget(BUDGET_FILE_NAME)
    expenses_to_save = False

    while True:
        print_header(total_expenses, budget)
        choice = get_menu_choice()

        if choice == MenuChoice.ADD_EXPENSE.value:
            expense = add_expense()
            expenses.append(expense)
            total_expenses += float(expense["Amount"])
            expenses_to_save = True
            print(f"Expense added successfully. {expense}")
            input("Press Enter to continue.....")

        elif choice == MenuChoice.VIEW_EXPENSE.value:
            view_expenses(expenses)
            input("Press Enter to continue.....")

        elif choice == MenuChoice.TRACK_BUDGET.value:
            print(f"Current budget amount is : {budget}")
            budget = float(input("Enter new budget: ") or budget)
            compare_budget(budget, total_expenses)
            save_budget(budget, BUDGET_FILE_NAME)
            input("Press Enter to continue.....")

        elif choice == MenuChoice.SAVE_EXPENSE.value:
            save_expenses(expenses, EXPENSE_FILE_NAME)
            expenses_to_save = False
            print("Expenses saved.")
            input("Press Enter to continue.....")

        elif choice == MenuChoice.EXIT.value:
            if expenses_to_save:
                save_expenses(expenses, EXPENSE_FILE_NAME)
            print("Thank you for using PET!!!")
            break

        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()