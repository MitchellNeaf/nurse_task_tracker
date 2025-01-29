import csv
import matplotlib.pyplot as plt

# File containing logged tasks
FILE_NAME = "nursing_tasks.csv"

def read_data():
    """Read task data from the CSV file."""
    data = []
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({
                    "Task Name": row["Task Name"],
                    "Category": row["Category"],
                    "Time Spent (minutes)": int(row["Time Spent (minutes)"])
                })
    except FileNotFoundError:
        print(f"Error: File '{FILE_NAME}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return data

def visualize_time_distribution(data):
    """Visualize time spent on tasks."""
    # Summarize total time by category
    category_time = {}
    for task in data:
        category = task["Category"]
        time_spent = task["Time Spent (minutes)"]
        category_time[category] = category_time.get(category, 0) + time_spent

    # Pie Chart
    categories = list(category_time.keys())
    times = list(category_time.values())

    plt.figure(figsize=(8, 6))
    plt.pie(times, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title("Time Distribution by Task Category")
    plt.show()

def visualize_medication_focus(data):
    """Compare time spent on medications vs other tasks."""
    total_time = sum(task["Time Spent (minutes)"] for task in data)
    med_time = sum(
        task["Time Spent (minutes)"]
        for task in data
        if task["Category"].lower() == "medications"
    )
    other_time = total_time - med_time

    # Bar Chart
    plt.figure(figsize=(8, 6))
    plt.bar(["Medications", "Other Tasks"], [med_time, other_time], color=["blue", "gray"])
    plt.title("Time Spent on Medications vs Other Tasks")
    plt.ylabel("Time Spent (minutes)")
    plt.show()

def main():
    data = read_data()
    if not data:
        print("No data available for visualization.")
        return

    print("\n--- Data Visualization ---")
    print("1. Pie Chart: Time Distribution by Task Category")
    print("2. Bar Chart: Medications vs Other Tasks")
    print("3. Exit")
    
    while True:
        choice = input("Choose a visualization (1-3): ")
        if choice == "1":
            visualize_time_distribution(data)
        elif choice == "2":
            visualize_medication_focus(data)
        elif choice == "3":
            print("Exiting visualization...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
