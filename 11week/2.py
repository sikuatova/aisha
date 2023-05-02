import psycopg2

def insert_or_update_user(name, phone):
    conn = psycopg2.connect(database="phonebook", user="aisha", password="30121995")
    cur = conn.cursor()
    cur.execute("SELECT phone FROM PhoneBook WHERE name=%s", (name,))
    result = cur.fetchone()
    if result:
        cur.execute("UPDATE PhoneBook SET phone=%s WHERE name=%s", (phone, name))
    else:
        cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    conn.close()
