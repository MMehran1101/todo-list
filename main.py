import json
import os


def get_input(input_text):
    choice = input(input_text)
    match choice:
        case '9':
            menu()
        case '1':
            show_tasks()
            get_input("Press \'9\' to go back to menu ... ")
        case '2':
            add_task()
            get_input("Press \'9\' to go back to menu ... ")
        case '3':
            delete_task()
            get_input("Press \'9\' to go back to menu ... ")
        case '4':
            exit()


def save_task():
    with open("data_todo.json", "w", encoding="utf-8") as f:
        json.dump(tasklist, f, ensure_ascii=False, indent=2)
    print("TASKS Saved !!")


def load_tasks():
    global tasklist
    if os.path.exists("data_todo.json"):
        with open("data_todo.json", "r", encoding="utf-8") as f:
            tasklist = json.load(f)
    else:
        tasklist = []


def show_tasks():
    if not tasklist:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasklist, start=1):
        print(f"{idx}. {task}")


def add_task():
    task = input("Write your task ... ")
    tasklist.append(task)
    save_task()

    m = input("Do you want add more task? (y/n)")
    if m == 'y':
        add_task()
    elif m == 'n':
        menu()
    else:
        print('Please enter current answer!')


def delete_task():
    show_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasklist):
            removed = tasklist.pop(task_number - 1)
            save_task()
            print(f"Deleted task: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")


def menu():
    print("\n   * The Mehran To-DO list Project *\n")
    print("-----------------")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    print("-----------------")
    get_input("Choose your action (1-4) : ")


tasklist = []
load_tasks()
menu()
