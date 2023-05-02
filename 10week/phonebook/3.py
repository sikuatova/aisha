import psycopg2

conn = psycopg2.connect(
    database="phonebook",
    user="aisha",
    password="30121995"
)

cursor = conn.cursor()

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
