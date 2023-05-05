import psycopg2
import csv

conn = psycopg2.connect("dbname=phonebook1 user=postgres password=30121995")
cursor = conn.cursor()

with open('pq1.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header row
    for row in reader:
        cursor.execute(
            "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)",
            (row[0], row[1], row[2])
        )
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
phone = input("Enter phone number: ")

cursor.execute(
    "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)",
    (first_name, last_name, phone)
)

user_id = input("Enter the ID of the contact you want to update: ")
new_first_name = input("Enter the new first name: ")
new_phone = input("Enter the new phone number: ")

cursor.execute(
    "UPDATE contacts SET first_name = %s, phone = %s WHERE id = %s",
    (new_first_name, new_phone, user_id)
)
conn.commit()
cursor.close()
conn.close()
