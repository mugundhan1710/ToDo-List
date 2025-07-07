import tkinter as tk
from tkinter import messagebox
tasks = []
def show_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    title = input("Enter task title: ")
    priority = input("Enter priority (High/Medium/Low): ")
    task = {
        "title": title,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks added yet.")
        return
    print("\n--- Task List ---")
    for i, task in enumerate(tasks):
        status = "✅" if task['completed'] else "❌"
        print(f"{i+1}. {task['title']} | Priority: {task['priority']} | Status: {status}")

def mark_completed():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as complete: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            deleted = tasks.pop(task_no - 1)
            print(f"Deleted task: {deleted['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def gui_add_task():
    title = entry_title.get()
    priority = priority_var.get()
    if not title:
        messagebox.showwarning("Missing Input", "Please enter a task title.")
        return
    task = {
        "title": title,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    entry_title.delete(0, tk.END)
    update_gui_task_list()

def gui_mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]['completed'] = True
        update_gui_task_list()

def gui_delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_gui_task_list()

def update_gui_task_list():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        listbox.insert(tk.END, f"{i}. [{status}] {task['title']} ({task['priority']})")
        
root = tk.Tk()
root.title("To-Do List (CLI + GUI)")
root.geometry("500x400")

tk.Label(root, text="Task Title:").pack()
entry_title = tk.Entry(root, width=40)
entry_title.pack()

tk.Label(root, text="Priority:").pack()
priority_var = tk.StringVar(value="Medium")
tk.OptionMenu(root, priority_var, "High", "Medium", "Low").pack()

tk.Button(root, text="Add Task", command=gui_add_task).pack(pady=5)
tk.Button(root, text="Mark Completed", command=gui_mark_done).pack(pady=5)
tk.Button(root, text="Delete Task", command=gui_delete_task).pack(pady=5)

listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

import threading

def run_cli():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List. Have a productive day!")
            break
        else:
            print("Invalid choice. Please try again.")

cli_thread = threading.Thread(target=run_cli)
cli_thread.start()
root.mainloop()