from constants import SCREEN_WIDTH

def print_border():
    """Prints a border line."""
    print("=" * SCREEN_WIDTH + "\n")

def is_valid_date(date_str: str) -> bool:
    """Checks if the input date follows the YYYY-MM-DD format."""
    from datetime import datetime
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_valid_amount(amount_str: str) -> bool:
    """Validates if the input amount is a positive float."""
    try:
        return float(amount_str) > 0
    except ValueError:
        return False