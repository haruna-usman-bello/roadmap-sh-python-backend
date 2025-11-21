"""Task Tracker CLI Application."""
import re
import json
from datetime import datetime

COMMANDS = ['add', 'update', 'delete', 'list', 'mark', 'exit']
STATUS_OPTIONS = ['todo', 'in-progress', 'done']

def task_file_load():
    """Load tasks from the tasks.json file."""
    try:
        with open('tasks.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
tasks = task_file_load()
def add_task(description):
    """Add a new task to the tracker."""
    status = 'todo'
    created_at = str(datetime.now())
    updated_at = str(datetime.now())
    new_task = {'id': len(tasks) + 1, 'description': description, 'status': status, 'created_at': created_at, 'updated_at': updated_at}
    tasks.append(new_task)

    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=2)
        print(f"Task added successfully: (ID: {new_task['id']})")


def list_tasks():
    """List all tasks in the tracker."""
   
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}")

def main():
    user_command = input("task-cli ")
    command = re.match(r'\S+', user_command).group(0)

    if command not in COMMANDS:
        print("Unknown command. Please try any of the following commands: add, update, delete, list, mark, exit")

    if command == 'add':
        description = user_command[len(f'{command} '):].strip('"\'')
        add_task(description)
    elif command == 'list':
        list_tasks()

if __name__ == '__main__':
    main()

