import tkinter as tk
from tkinter import messagebox
def add_task():
    task = entry.get()
    if task:
        tasks.insert(tk.END, task)
        entry.delete(0,tk.END)
def edit_task():
    try:
        selected_task = tasks.curselection()[0]
        current_task = tasks.get(selected_task)
        entry.delete(0,tk.END)
        entry.insert(tk.END, current_task)
        tasks.delete(selected_task)
    except IndexError:
        pass
def delete_task():
    try:
        selected_task = tasks.curselection()[0]
        tasks.delete(selected_task)
    except IndexError:
        pass
root = tk.Tk()
root.title("Todo List")
frame = tk.Frame(root)
frame.pack(pady=10)
tasks = tk.Listbox(frame,width=50 ,height = 10)
tasks.pack(side=tk.TOP, fill=tk.BOTH,expand=1)
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
button_frame = tk.Frame(root)
button_frame.pack()
add_button = tk.Button(button_frame,text="Add Task",command=add_task)
add_button.pack(side=tk.LEFT,padx=5)
edit_button = tk.Button(button_frame,text="Edit Task",command=edit_task)
edit_button.pack(side = tk.LEFT,padx=5)
delete_button = tk.Button(button_frame,text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT,padx=5)
root.mainloop()