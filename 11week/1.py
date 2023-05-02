import psycopg2

def search_records(pattern):
    conn = psycopg2.connect(database="phonebook", user="aisha", password="30121995")
    cur = conn.cursor()
    query = f"SELECT * FROM PhoneBook WHERE name LIKE '%{pattern}%' OR surname LIKE '%{pattern}%' OR phone LIKE '%{pattern}%'"
    cur.execute(query)
    records = cur.fetchall()
    conn.close()
    return records
