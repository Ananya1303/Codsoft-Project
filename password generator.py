import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def on_generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive integer for the length")
            return
        password = generate_password(length)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error","Invalid input")
root = tk.Tk()
root.title("Password Generator")
length_label = tk.Label(root, text="Enter the desired length of the password")
length_label.pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack(pady=10)
generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)
password_label = tk.Label(root, text="Generate Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(root)
password_entry.pack(pady=10)
root.mainloop()
