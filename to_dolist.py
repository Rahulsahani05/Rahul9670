import json
import os

FILENAME = "tasks.json"
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []
# Save tasks to file.
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Show all tasks.
def show_tasks(tasks):
    if not tasks:
        print("\n Your to-do list is empty.")
    else:
        print("\n Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task['done'] else "Pending"
            print(f"{i}. {task['title']} [{status}]")
# Add a new task.
def add_task(tasks):
    title = input("\nEnter the task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Update the task.
def update_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to update: "))
        new_title = input("Enter new task description: ")
        tasks[task_num - 1]['title'] = new_title
        save_tasks(tasks)
        print("Task updated successfully!")
    except (IndexError, ValueError):
        print(" Invalid task number!")

# Mark task  done.
def mark_done(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to mark as done: "))
        tasks[task_num - 1]['done'] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Delete the task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to delete: "))
        tasks.pop(task_num - 1)
        save_tasks(tasks)
        print("Task deleted!")
    except (IndexError, ValueError):
        print("Invalid task number!")
def main():
    tasks = load_tasks()
    while True:
        print("\n---  To-Do List Menu ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Mark task done")
        print("5. Delete task")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Your tasks are saved.")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")
if __name__ == "__main__":
    main()