from datetime import datetime
from constants import LOG_FILE_NAME, LogType

def log_data(message: str, log_type: LogType):
    """Writes a log message to the log file."""
    try:
        with open(LOG_FILE_NAME, "a") as file:
            file.write(f"{datetime.now()}: {log_type.name}: {message}\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")