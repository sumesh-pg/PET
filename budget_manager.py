import os
from logger import log_data
from constants import LogType

def load_budget(file_name: str) -> float:
    """Loads the budget from a file."""
    budget = 0
    if not os.path.exists(file_name):
        log_data(f"Budget File not found - {file_name}", LogType.WARNING)
        return budget

    try:
        with open(file_name, "r") as file:
            budget = float(file.read().strip())
    except ValueError:
        log_data("Invalid budget data", LogType.ERROR)

    return budget

def save_budget(budget: float, file_name: str):
    """Saves the budget to a file."""
    try:
        with open(file_name, "w") as file:
            file.write(f"{budget:.2f}")
        log_data("Budget saved successfully", LogType.INFORMATION)
    except Exception as e:
        log_data(f"Error saving budget: {e}", LogType.ERROR)

def compare_budget(budget: float, total_expense: float):
    """Compares expenses with the budget."""
    difference = budget - total_expense
    if difference < 0:
        print(f"\nYou have exceeded your budget by {-difference:.2f}")
    else:
        print(f"\nYou have {difference:.2f} left in your budget")