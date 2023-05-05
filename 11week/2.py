import psycopg2

def insert_or_update_user(name, phone):
    conn = psycopg2.connect(database="phonebook1", user="aisha", password="30121995")
    cur = conn.cursor()
    cur.execute("SELECT phone FROM contacts WHERE first_name=%s", (name,))
    result = cur.fetchone()
    if result:
        cur.execute("UPDATE contacts SET phone=%s WHERE first_name=%s", (phone, name))
    else:
        cur.execute("INSERT INTO contacts (first_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    conn.close()
