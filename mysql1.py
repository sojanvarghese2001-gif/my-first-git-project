import tkinter as tk
from tkinter import messagebox
from sql_connect  import insert_data
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    if not name or not email or not age:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return
    insert_data(name,email,age)
    messagebox.showinfo("Form Submitted",
                        f"Name: {name}\nEmail: {email}\nAge: {age}")

# Main window
root = tk.Tk()
root.title("User Data Form")
root.geometry("300x250")

# Labels and entry fields
tk.Label(root, text="Name").pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Email").pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack()

tk.Label(root, text="Age").pack(pady=5)
age_entry = tk.Entry(root, width=30)
age_entry.pack()

# Submit button
tk.Button(root, text="Submit", command=submit_form).pack(pady=20)

root.mainloop()



