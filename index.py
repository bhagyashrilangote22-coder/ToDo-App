"""A simple command-line to-do list app.

Run with:  python todo.py
Tasks are saved in tasks.json in the same folder.
"""

import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """Read tasks from the file. Return an empty list if there is no file yet."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    """Write the task list to the file."""
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Add one!")
        return
    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        mark = "[x]" if task["done"] else "[ ]"
        print(f"  {number}. {mark} {task['title']}")


def add_task(tasks):
    title = input("Task name: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Task name can't be empty.")


def complete_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Number of task to mark done: "))
        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("Nice work!")
    except (ValueError, IndexError):
        print("Please enter a valid task number.")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Number of task to delete: "))
        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print("Please enter a valid task number.")


def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do App ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Quit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()