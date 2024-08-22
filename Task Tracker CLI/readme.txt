# Task Management System

Task Management System is a command-line application that allows users to manage tasks using a JSON file. Users can add, update, delete, and list tasks, as well as mark them with different statuses.

## Features

- **Add Task**: Add a new task with a description.
- **Update Task**: Update the description of an existing task.
- **Delete Task**: Remove a task from the list.
- **Mark Task**: Change the status of a task (e.g., to-do, in-progress, done).
- **List Tasks**: View all tasks or filter by status.

## Requirements

- Python 3.5.X

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Doomzes/roadmap_projects/blob/d0c03efbad4ffe83f7a5fe9bec9229815db29af3/Task%20Tracker%20CLI/main.py
    ```
2. Navigate to the project directory:
    ```bash
    cd <project-directory>
    ```
3. https://roadmap.sh/projects/task-tracker


### Command-Line Arguments

| Command           | Description                                   | Example Usage                                |
|-------------------|-----------------------------------------------|----------------------------------------------|
| `add`             | Add a new task                                | `python main.py add "Buy groceries"`         |
| `update`          | Update an existing task                       | `python main.py update 1 "Cook dinner"`      |
| `delete`          | Delete a task                                 | `python main.py delete 1`                    |
| `mark-in-progress`| Mark a task as in-progress                    | `python main.py mark-in-progress 1`          |
| `mark-done`       | Mark a task as done                           | `python main.py mark-done 1`                 |
| `mark-todo`       | Mark a task as to-do                          | `python main.py mark-todo 1`                 |
| `list`            | List all tasks                                | `python main.py list`                        |
| `list done`       | List tasks marked as done                     | `python main.py list done`                   |
| `list in-progress`| List tasks marked as in-progress              | `python main.py list in-progress`            |
| `list todo`       | List tasks marked as to-do                    | `python main.py list todo`                   |
