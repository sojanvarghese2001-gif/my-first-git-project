import tkinter as tk
from tkinter import ttk
from sql_connect import fetch_data

root = tk.Tk()
root.title("form records")
root.geometry("700x400")

columns = ("Name", "email", "Age")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Setup headings
for column in columns:
    tree.heading(column, text=column)
    tree.column(column, anchor="center", width=150)

# Scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# PACK THEM (YOU MISSED THIS PART)
tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Fetch Data
data = fetch_data()

for row in data:
    tree.insert("", "end", values=row)

root.mainloop()
