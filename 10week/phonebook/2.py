import psycopg2

conn = psycopg2.connect(
    database="phonebook",
    user="aisha",
    password="30121995"
)


cursor = conn.cursor()

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
phone = input("Enter phone number: ")

cursor.execute(
    "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)",
    (first_name, last_name, phone)
)

conn.commit()
cursor.close()
conn.close()
