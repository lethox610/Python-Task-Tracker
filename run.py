import sys
import json

"""
run.py --add <title> <details>
run.py --list
run.py --update <id>
run.py --delete <id>
run.py --help
"""

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

def delete_task(id):
    """
    - Find the task by ID and remove it from the list.
    """

# Add a new task
add_task("Clean the house", "Focus on the living room and kitchen.")

# List all tasks
view_tasks()