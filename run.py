import argparse
import json
import os



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

TASKS_DB = "tasks.json"

def initialize_db():
    if not os.path.exists(TASKS_DB):
        with open(TASKS_DB, "w") as f:
            json.dump({}, f)

def load_tasks():
    if os.path.exists(TASKS_DB):
        with open(TASKS_DB, "r") as f:
            return json.load(f)
    return {}

def save_tasks(tasks):
    with open(TASKS_DB, "w") as f:
        json.dump(tasks, f, indent=4)

tasks = load_tasks()

def add_task(title, details):
    tasks = load_tasks()
    new_id = max(map(int, tasks.keys()), default=0) + 1
    tasks[str(new_id)] = {"title": title, "details": details, "status": "pending"}
    save_tasks(tasks)
    print(f"Task added successfully! Task ID: {new_id}")

def view_tasks():
    for task_id, task in tasks.items():
        print("--------------------------")
        print(f"Task ID: {task_id}")
        print(f"Title: {task['title']}")
        print(f"Details: {task['details']}")
        print(f"Status: {task['status']}")

def update_task(id):
    tasks = load_tasks()
    task_id_str = str(id)

    if task_id_str in tasks:
        task = tasks[task_id_str]
        print("Current task details:")
        for key, value in task.items():
            print(f"{key.capitalize()}: {value}")

        field = input("Which field do you want to update? (title, details, status): ").strip().lower()
        if field not in task:
            print("Invalid field. PLease choose from 'title', 'details', or 'status'")
            return
        
        new_value = input(f"Enter new value for {field}: ").strip()
        task[field] = new_value

        save_tasks(tasks)
        print(f"Task updated successfully! New {field}: {task[field]}")
    else:
        print(f"Task with ID {id} not found.")

def delete_task(id):
    task_id_str = str(id)
    
    if task_id_str in tasks:
        conf = input(f"Are you sure you want to delete task with ID {id}? (Y/N):").capitalize()
        if conf == 'Y':
            del tasks[task_id_str]
            save_tasks(tasks)
            print("Task deleted successfully")
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