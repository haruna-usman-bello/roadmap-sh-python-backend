"""Task Tracker CLI Application."""

import re
from task_tracker import TaskTracker


def main():
    """Main function to run the CLI application"""
    tracker = TaskTracker()
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
                tracker.add_task(description)
            case 'list':
                status_filter = user_command[len(f'{command} '):].strip()
                tracker.list_tasks(
                    status_filter=status_filter if status_filter else None)
            case 'update':
                items = user_command[len(f'{command} '):].split(' ', 1)
                if len(items) < 2:
                    print("Please provide both task ID and new description.")
                    continue
                task_id = int(items[0])
                description = items[1].strip('"\'')
                tracker.update_task(task_id, description)
            case 'delete':
                try:
                    task_id = int(user_command[len(f'{command} '):].strip())
                except ValueError:
                    print("Please provide a valid task ID.")
                    continue
                tracker.delete_task(task_id)
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
                tracker.mark_task(task_id, status)
            case _:
                print(
                    "Unknown command. Please try any of the following commands: add, update, delete, list, mark, exit")

    print("exiting Task Tracker CLI. Goodbye!")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting Task Tracker CLI. Goodbye!")
