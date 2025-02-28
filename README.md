# Personal Expense Tracker (PET)

## Overview

The **Personal Expense Tracker (PET)** is a Python-based command-line application designed to help users manage and track their daily expenses efficiently. It offers functionalities to add expenses, view recorded transactions, set and monitor budgets, and save expense data for future reference.

## Features

- **Add Expense:** Input details such as date, category, amount, and description for each expense.
- **View Expenses:** Display all recorded expenses in a structured format.
- **Track Budget:** Set a budget and compare it against total expenses to monitor spending.
- **Save Expenses:** Persist expense data to a file for future access.
- **Logging System:** Maintain logs for warnings, errors, and informational messages to track system activities.

## Installation

### Prerequisites

- Python 3.x installed on your system.

### Clone the Repository

```sh
git clone https://github.com/sumesh-pg/PET.git
cd PET
```

## Usage

Run the program using:

```sh
python PET.py
```

### Menu Options

1. **Add Expense** – Add a new expense entry.
2. **View Expenses** – View all recorded expenses.
3. **Track Budget** – Set and monitor your budget.
4. **Save Expenses** – Save expense data to a file.
5. **Exit** – Exit the application.

## File Structure

- `PET.py` – Main script containing the application logic.
- `data/expenses.txt` – File to store recorded expenses.
- `data/budget.txt` – File to store the budget amount.
- `logs/logs.txt` – Log file for warnings, errors, and informational messages.
- `budget_manager.py` – Module handling budget-related functionalities.
- `expense_manager.py` – Module managing expense operations.
- `logger.py` – Module for logging system activities.
- `constants.py` – Module defining constant values used across the application.
- `utils.py` – Module containing utility functions.

## Logging System

The application maintains a log file at `logs/logs.txt` to record:

- **WARNING:** Issues like missing files or potential problems.
- **ERROR:** Errors such as invalid data formats or unexpected exceptions.
- **INFORMATION:** General information like successful budget updates or data saves.

## Contributing

Contributions are not welcome! This is an academic project for submission.

## License

This project is open-source and available under the MIT License.

## Author

[Sumesh Gopalakrishnan](https://github.com/sumesh-pg)

