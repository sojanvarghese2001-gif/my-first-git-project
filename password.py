import csv
import os

filename = "product_data.csv"
header = ["product", "price", "date", "quantity", "city"]

# Create the file and write header if it doesn't exist
if not os.path.exists(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

# Loop for user input
while True:
    product = input("Enter product name: ")
    price = input("Enter price: ")
    date = input("Enter date (YYYY-MM-DD): ")
    quantity = input("Enter quantity: ")
    city = input("Enter city: ")

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([product, price, date, quantity, city])

    cont = input("Do you want to add another entry? (yes/no): ").strip().lower()
    if cont != 'yes':
        break

print(f"Data entry completed. Entries saved to {filename}.")
