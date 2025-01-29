import csv
import os

# File to store task data
FILE_NAME = "nursing_tasks.csv"

# Ensure the CSV file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Task Name", "Category", "Time Spent (minutes)"])

def log_task():
    """Log a new task."""
    print("\n--- Log a New Task ---")
    task_name = input("Enter the task name: ")
    category = input("Enter the category (e.g., Patient Care, Charting, Admin): ")
    try:
        time_spent = int(input("Enter time spent (in minutes): "))
    except ValueError:
        print("Invalid input for time. Please enter an integer.")
        return

    # Save to CSV
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([task_name, category, time_spent])
    
    print(f"Task '{task_name}' logged successfully!\n")

def view_tasks():
    """View all logged tasks."""
    print("\n--- Logged Tasks ---")
    if not os.path.exists(FILE_NAME) or os.stat(FILE_NAME).st_size == 0:
        print("No tasks logged yet.")
        return
    
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print("\t".join(row))
    print()

def main():
    """Main menu for the task logger."""
    while True:
        print("\n--- Nursing Workflow Tracker ---")
        print("1. Log a new task")
        print("2. View logged tasks")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            log_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
