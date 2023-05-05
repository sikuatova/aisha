import psycopg2

def search_records(pattern):
    conn = psycopg2.connect(database="phonebook1", user="aisha", password="30121995")
    cur = conn.cursor()
    query = f"SELECT * FROM contacts WHERE first_name LIKE '%{pattern}%' OR lat_namename LIKE '%{pattern}%' OR phone LIKE '%{pattern}%'"
    cur.execute(query)
    records = cur.fetchall()
    conn.close()
    return records
