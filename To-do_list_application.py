import os

TODO_FILE = "todo.txt"

def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add New Task")
    print("3. Remove Task")
    print("4. Exit")

def view_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\nTo-Do List:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task.strip()}")
            else:
                print("\nYour to-do list is empty.")
    else:
        print("\nYour to-do list is empty.")

def add_task():
    task = input("Enter the task: ")
    with open(TODO_FILE, "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added to the to-do list.")

def remove_task():
    view_todo_list()
    try:
        task_num = int(input("Enter the task number to remove: "))
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1).strip()
            with open(TODO_FILE, "w") as file:
                file.writelines(tasks)
            print(f"Task '{removed_task}' removed from the to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
