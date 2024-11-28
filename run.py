import argparse
import json



parser = argparse.ArgumentParser(description="CLI Task Tracker")

# Add a new task
parser.add_argument('--add', nargs=2, metavar=('title', 'details'), help='Add a new task with a title and details')

# List all tasks
parser.add_argument('--list', action='store_true', help='List all tasks')

# Update task
parser.add_argument('--update', type=int, metavar='id', help='Update a task by its ID')

# Delete a task
parser.add_argument('--delete', type=int, metavar='id', help='Delete a task by its ID')

# Parse arguments
args = parser.parse_args()

tasks = {
    1: {"title": "Buy groceries", "details": "Milk, eggs, bread", "status": "pending"},
    2: {"title": "Study Python", "details": "Complete the CLI project", "status": "completed"},
}


def add_task(title, details):
    """
    - Generate a unique ID.
    - Append the task to the list.
    """
    new_id = max(tasks.keys()) + 1
    tasks[new_id] = {
        "title": title,
        "details": details,
        "status": "pending",
    }

def view_tasks():
    """
    - Loop through the list and display tasks in readable format.
    - Highlight completed tasks differently if desired
    """
    for task_id, task in tasks.items():
        print("--------------------------")
        print(f"Task ID: {task_id}")
        print(f"Title: {task['title']}")
        print(f"Details: {task['details']}")
        print(f"Status: {task['status']}")

def update_task(id):
    """
    - Find the task by ID.
    - Let user update fields (e.g. mark as completed or change details).
    """
    task = tasks.get(id)
    if task:
        print("Current task details:")
        for key, value in task.items():
            print(f"{key.capitalize()}: {value}")
        
        field = input("Which field do you want to update? (title, details, status): ").strip().lower()
        if field not in task:
            print("Invalid field. Please choose from 'title', 'details' or 'status'.")
            return
        new_value = input(f"Enter new value for {field}: ").strip()
        task[field] = new_value
        print(f"Task updated successfully! New field {field}: {task[field]}")
    else:
        print(f"Task with ID {id} not found.")

def delete_task(id):
    """
    - Find the task by ID and remove it from the list.
    """
    task = tasks.get(id)
    if task:
        conf = input(f"Are you sure you want to delete task with ID {id}? (Y/N):").capitalize()
        if conf == 'Y':
            print("Task deleted successfully")
            tasks.pop(id)
        elif conf == 'N':
            return
        else:
            print("Invalid input.")
    else:
        print(f"Task with ID {id} not found.")

if args.add:
    title, details = args.add
    print(f"Adding task: {title} - {details}")
    add_task(title=title, details=details)
elif args.list:
    view_tasks()
elif args.update:
    task_id = args.update
    update_task(task_id)
elif args.delete:
    task_id = args.delete
    delete_task(task_id)