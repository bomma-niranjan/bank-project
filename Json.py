import json
import os

# ------------------- Task Class -------------------

class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

# ------------------- File Handling -------------------

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

def load_tasks(filename='tasks.json'):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        data = json.load(f)
        return [Task(**item) for item in data]

# ------------------- Display Function -------------------

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "✔" if task.completed else "✘"
        print(f"{idx}. [{status}] {task.title} - {task.category}")
        print(f"   Description: {task.description}")
    print()

# ------------------- Main CLI Interface -------------------

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category (Work/Personal/Urgent): ")
            tasks.append(Task(title, description, category))
            print("Task added successfully!")

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            display_tasks(tasks)
            try:
                task_num = int(input("Enter task number to mark as completed: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1].mark_completed()
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            display_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task.title}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# ------------------- Entry Point -------------------

if __name__ == "__main__":
    main()
