# Simple To-Do List App

tasks = []

def show_menu():
    print("\n----- TO-DO LIST MENU -----")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Exit")


while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    # Add task
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print(f"'{task}' added to your to-do list!")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    # Remove task
    elif choice == "3":
        if len(tasks) == 0:
            print("No task to remove!")
        else:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")

    # Exit application
    elif choice == "4":
        print("Goodbye! Have a productive day.")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
