"""Task Tracker CLI Application."""
import re
import json
from datetime import datetime

COMMANDS = ['add', 'update', 'delete', 'list', 'mark', 'exit']
STATUS_OPTIONS = ['todo', 'in-progress', 'done']

def add_task(description):
    """Add a new task to the tracker."""
    status = 'todo'
    created_at = str(datetime.now())
    updated_at = str(datetime.now())

    with open('tasks.json', 'r', encoding='utf-8') as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = []

    new_task = {'id': len(tasks) + 1, 'description': description, 'status': status, 'created_at': created_at, 'updated_at': updated_at}
    tasks.append(new_task)

    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=2)
        print(f"Task added successfully: (ID: {new_task['id']})")

def main():
    user_command = input("task-cli ")
    command = re.match(r'\S+', user_command).group(0)

    if command not in COMMANDS:
        print("Unknown command. Please try any of the following commands: add, update, delete, list, mark, exit")

    if command == 'add':
        description = user_command[len(f'{command} '):].strip('"\'')
        add_task(description)

if __name__ == '__main__':
    main()

