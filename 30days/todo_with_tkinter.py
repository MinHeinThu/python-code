import tkinter as tk
from tkinter import messagebox

# Functionality
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning('Input Error', 'You must enter a task!')

def delete_task():
    try:
        index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(index)
    except IndexError:
        messagebox.showwarning('Selection Error', 'No task selected')

def modify_task():
    try:
        index = tasks_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            tasks_listbox.delete(index)
            tasks_listbox.insert(index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning('Input Error', 'Enter a new task to modify!')
    except IndexError:
        messagebox.showwarning('Selection Error', 'No tsk selected!')

# Main window
root = tk.Tk()
root.title('To-do List App')

# Entry Box
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

add_button = tk.Button(button_frame, text='Add Task', command=add_task)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text='Delete Task', command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

modify_button = tk.Button(button_frame, text="Modify Task", command=modify_task)
modify_button.grid(row=0, column=2, padx=5)

# Listbox
tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.pack(pady=10)

root.mainloop()