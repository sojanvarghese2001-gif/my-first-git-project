import mysql.connector
from tkinter import messagebox

def insert_data(name, email, age):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Sojan@2001",
            database="my_db1"   # <-- your correct database name
        )

        mycursor = mydb.cursor()

        # Correct SQL query
        query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
        val = (name, email, age)

        mycursor.execute(query, val)
        mydb.commit()

        mycursor.close()
        mydb.close()

        messagebox.showinfo("Success", "Data Inserted Successfully")

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"MySQL Error: {error}")


def fetch_data():
    try:
        mydb = mysql.connector.connect(
			host="localhost",
			port=3306,
			user="root",
			password="Sojan@2001",
			database="my_db1"  # <-- your correct database name
		)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT *FROM users")
        records = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return records
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"MySQL Error: {error}")
        return[]