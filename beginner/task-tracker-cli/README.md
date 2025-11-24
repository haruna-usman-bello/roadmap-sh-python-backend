# Task Tracker CLI

A simple command-line application built with Python to efficiently manage your daily tasks. This tool allows you to add, update, delete, and track the status of your tasks directly from your terminal. All tasks are saved locally in a `tasks.json` file.

## Project URL

<https://roadmap.sh/projects/task-tracker>

## Features

- **Add Tasks**: Quickly add new tasks with a description.
- **List Tasks**: View all your tasks, or filter them by status: `todo`, `in-progress`, `done`.
- **Update Tasks**: Modify the description of any existing task using its ID.
- **Delete Tasks**: Remove tasks by their ID.
- **Change Status**: Mark tasks as `in-progress` or `done` to track your progress.
- **Data Persistence**: Your tasks are automatically saved to `tasks.json`.
- **Help Menu**: An in-built help command to display all available commands.

## Getting Started

### Prerequisites

- Python 3

### Installation

No installation is required. Simply ensure the project files (`app.py`, `task_tracker.py`) are in the same directory.

### Running the Application

To start the task tracker, run the following command in your terminal:

```sh
python app.py
```

The application will launch and display the available commands.

## Usage

Once the application is running, you can use the following commands:

- **Add a new task:**

    ```sh
    add "Describe your new task here"
    ```

- **List all tasks:**

    ```sh
    list
    ```

- **List tasks with a specific status:**

    ```sh
    list todo
    list in-progress
    list done
    ```

- **Update a task's description:**

    ```sh
    update <task_id> "New updated description"
    ```

    *Example:* `update 1 "Submit the final report"`

- **Delete a task:**

    ```sh
    delete <task_id>
    ```

    *Example:* `delete 3`

- **Mark a task's status:**

    ```sh
    mark <status> <task_id>
    ```

    *Examples:*

    ```sh
    mark in-progress 1
    mark done 2
    ```

- **Show the help manual:**

    ```sh
    help
    ```

- **Exit the application:**

    ```sh
    exit
    ```

## Testing

The project includes a suite of unit tests to verify the functionality of the task tracker. To run the tests, execute the following command:

```sh
python test_app.py
