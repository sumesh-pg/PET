
from enum import Enum, auto

# File Paths
EXPENSE_FILE_NAME = "data/expenses.txt"
BUDGET_FILE_NAME = "data/budget.txt"
LOG_FILE_NAME = "logs/logs.txt"
PRINT_DATE_WIDTH = 10
PRINT_CATEGORY_WIDTH = 25
PRINT_AMOUNT_WIDTH = 15

# UI Settings
SCREEN_WIDTH = 100

# Enum for log types
class LogType(Enum):
    WARNING = auto()
    ERROR = auto()
    INFORMATION = auto()

# Enum for Menu choices
class MenuChoice(Enum):
    ADD_EXPENSE = "1"
    VIEW_EXPENSE = "2"
    TRACK_BUDGET = "3"
    SAVE_EXPENSE = "4"
    EXIT = "5"