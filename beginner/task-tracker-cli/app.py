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


def save_tasks(tasks):
    """Write the current tasks to the tasks.json file."""
    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=2)


def add_task(description, tasks):
    """Add a new task to the tracker."""
    status = 'todo'
    created_at = str(datetime.now())
    updated_at = str(datetime.now())
    new_task = {'id': len(tasks) + 1, 'description': description,
                'status': status, 'created_at': created_at, 'updated_at': updated_at}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully: (ID: {new_task['id']})")


def list_tasks(status_filter=None, tasks=None):
    """List all tasks in the tracker."""
    if not tasks:
        print("No tasks found.")
        return
    if status_filter and status_filter in STATUS_OPTIONS:
        filtered_tasks = [
            task for task in tasks if task['status'] == status_filter]
    else:
        filtered_tasks = tasks

    for task in filtered_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['created_at'].split('.')[0]}, Updated At: {task['updated_at'].split('.')[0]}")


def update_task(task_id, description, tasks):
    """Update a task in the tracker."""
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updated_at'] = str(datetime.now())
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) updated successfully.")
            return
    print(f"Task with ID {task_id} not found.")


def delete_task(task_id, tasks):
    """Delete a task from the tracker."""
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) deleted successfully.")
            return
    print(f"Task with ID {task_id} not found.")


def mark_task(task_id, status, tasks):
    """Mark a task with a new status."""
    if status not in STATUS_OPTIONS:
        print(f"Invalid status. Choose from: {', '.join(STATUS_OPTIONS)}")
        return
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updated_at'] = str(datetime.now())
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) marked as {status} successfully.")
            return
    print(f"Task with ID {task_id} not found.")


def main():
    """Main function to run the CLI application."""
    tasks = task_file_load()
    command = ''
    while command != 'exit':
        user_command = input("task-cli ")
        try:
            command = re.match(r'\S+', user_command).group(0).lower()
        except AttributeError:
            print("Please enter a command.")
            continue
        match command:
            case 'exit':
                break
            case 'add':
                description = user_command[len(f'{command} '):].strip('"\'')
                if not description:
                    print("Description cannot be empty.")
                    continue
                add_task(description, tasks)
            case 'list':
                status_filter = user_command[len(f'{command} '):].strip()
                list_tasks(
                    status_filter=status_filter if status_filter else None, tasks=tasks)
            case'update':
                items = user_command[len(f'{command} '):].split(' ', 1)
                if len(items) < 2:
                    print("Please provide both task ID and new description.")
                    continue
                task_id = int(items[0])
                description = items[1].strip('"\'')
                update_task(task_id, description, tasks)
            case 'delete':
                try:
                    task_id = int(user_command[len(f'{command} '):].strip())
                except ValueError:
                    print("Please provide a valid task ID.")
                    continue
                delete_task(task_id, tasks)
            case 'mark':
                items = user_command[len(f'{command} '):].split(' ', 1)
                if len(items) < 2:
                    print("Please provide both task ID and status.")
                    continue
                try:
                    task_id = int(items[1])
                except ValueError:
                    print("Please provide a valid task ID.")
                    continue
                status = items[0].strip()
                mark_task(task_id, status, tasks)
            case _:
                print(
                    "Unknown command. Please try any of the following commands: add, update, delete, list, mark, exit")

    print("exiting Task Tracker CLI. Goodbye!")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting Task Tracker CLI. Goodbye!")
