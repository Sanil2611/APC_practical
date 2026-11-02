import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x150")

label = tk.Label(root, text="Welcome to Python packages!")
label.pack(pady=15)

button = tk.Button(root, text="Click Me",
                   command=lambda: messagebox.showinfo("Message", "Button clicked!"))
button.pack()

root.mainloop()
