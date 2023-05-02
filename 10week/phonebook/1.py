import psycopg2
import csv


conn = psycopg2.connect(
    database="phonebook",
    user="aisha",
    password="30121995"
)

cursor = conn.cursor()

with open('pq1.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header row
    for row in reader:
        cursor.execute(
            "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)",
            (row[0], row[1], row[2])
        )

conn.commit()
cursor.close()
conn.close()
