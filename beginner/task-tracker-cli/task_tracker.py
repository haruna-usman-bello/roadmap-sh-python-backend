"""Task Tracker CLI Application."""

import json
from datetime import datetime


class TaskTracker:
    """Task Tracker CLI Application."""

    COMMANDS = {'add', 'update', 'delete', 'list', 'mark', 'exit'}
    STATUS_OPTIONS = {'todo', 'in-progress', 'done'}

    def __init__(self):
        self.tasks = self.load_tasks()

    def show_avalible_flags(self) -> None:
        """Display available command flags."""
        print("A CLI application to efficiently manage your tasks\n")
        print("Available commands:")
        print("\tadd <str:description> - add new task to your tasks")
        print(
            "\tupdate <int:id> <str:description> - update task by id. Replace old to new description"
        )
        print("\tdelete <int:id> - delete task by id")
        print("\tmark in-progress <int:id> - replace  status to in-progress")
        print("\tmark done <int:id> - replace status to done")
        print("\tlist - to print all tasks")
        print("\tlist done - to print all tasks with status done")
        print("\tlist todo - to print all tasks with status todo")
        print("\tlist in-progress - to print all tasks with status in-progress")
        print("\thelp - to print this help manual")

    def load_tasks(self) -> list:
        """Load tasks from the tasks.json file."""
        try:
            with open('tasks.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self, tasks: list):
        """Write the current tasks to the tasks.json file."""
        with open('tasks.json', 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=2)

    def add_task(self, description: str):
        """Add a new task to the tracker"""
        status = 'todo'
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()
        last_task = self.tasks[-1] if self.tasks else None

        new_task = {'id': last_task['id'] + 1 if last_task else 1, 'description': description,
                    'status': status, 'created_at': created_at, 'updated_at': updated_at}
        self.tasks.append(new_task)
        self.save_tasks(self.tasks)
        print(f"Task added successfully: (ID: {new_task['id']})")

    def list_tasks(self, status_filter: str = None):
        """List all tasks in the tracker"""
        if not self.tasks:
            print("No tasks found.")
            return
        if status_filter and status_filter in self.STATUS_OPTIONS:
            filtered_tasks = [
                task for task in self.tasks if task['status'] == status_filter]
        else:
            filtered_tasks = self.tasks

        for task in filtered_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['created_at'].split('T')[0]}, Updated At: {task['updated_at'].split('T')[0]}")

    def update_task(self, task_id: int, description: str):
        """Update a task in the tracker"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['description'] = description
                task['updated_at'] = datetime.now().isoformat()
                self.save_tasks(self.tasks)
                print(f"Task (ID: {task_id}) updated successfully.")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id: int):
        """Delete a task from the tracker"""
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks(self.tasks)
                print(f"Task (ID: {task_id}) deleted successfully.")
                return
        print(f"Task with ID {task_id} not found.")

    def mark_task(self, task_id: int, status: str):
        """Mark a task with a new status"""
        if status not in self.STATUS_OPTIONS:
            print(
                f"Invalid status. Choose from: {', '.join(self.STATUS_OPTIONS)}")
            return
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = status
                task['updated_at'] = datetime.now().isoformat()
                self.save_tasks(self.tasks)
                print(f"Task (ID: {task_id}) marked as {status} successfully.")
                return
        print(f"Task with ID {task_id} not found.")
