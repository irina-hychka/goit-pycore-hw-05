import sys
from pathlib import Path


def parse_log_line(line: str) -> dict:
    """
    Parses a single line of the log and returns a dictionary
    with the following components:
    - date;
    - time;
    - log level;
    - message.
    """
    parts = line.split(" ", 3)
    if len(parts) < 4:
        return {}
    date, time, level, message = parts
    return {
        "date": date,
        "time": time,
        "level": level.strip(),
        "message": message.strip()
    }


def load_logs(file_path: Path) -> list:
    """
    Loads logs from a file and parses each line.
    """
    logs = []
    try:
        with file_path.open("r") as file:
            for line in file:
                log = parse_log_line(line)
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        sys.exit(1)
    
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filters logs by logging level.
    """
    return [log for log in logs if log["level"].lower() == level.lower()]


def count_logs_by_level(logs: list) -> dict:
    """
    Counts the number of records for each logging level.
    """
    counts = {"INFO": 0, "ERROR": 0, "DEBUG": 0, "WARNING": 0}
    for log in logs:
        level = log["level"].upper()
        if level in counts:
            counts[level] += 1
    return counts


def display_log_counts(counts: dict):
    """
    Formats and outputs calculation results and looks like a table.
    """
    print(f"\n{'Рівень логування':<20} | {'Кількість'}")
    print("-" * 19 + "- | -" + "-" * 8)
    for level, count in counts.items():
        print(f"{level:<20} | {count}")
    print("\n")


def display_log_details(logs: list, level: str):
    """
    Displays log details for a specific level.
    """
    print(f"Деталі логів для рівня '{level.upper()}':")
    
    for log in logs:
        if log["level"].lower() == level.lower():
            print(f"{log['date']} {log['time']} - {log['message']}")
    print("\n")


def main():
    """
    The main function for command line processing.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [level]")
        sys.exit(1)
    
    log_file_path = Path(sys.argv[1])
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None
    
    logs = load_logs(log_file_path)
    
    # Counting the number of logs by level
    log_counts = count_logs_by_level(logs)
    
    # Output of calculation results
    display_log_counts(log_counts)
    
    # If there is a level filter
    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        display_log_details(filtered_logs, level_filter)

# Usage
if __name__ == "__main__":
    main()
# Calling Example in terminal (from folder with files)
# python task_3.py logs.txt error