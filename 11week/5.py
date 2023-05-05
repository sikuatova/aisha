import psycopg2

def delete_by_name_or_phone(table_name, identifier):
    conn = psycopg2.connect(database="phonebook1", user="aisha", password="30121995")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {table_name} WHERE first_name='{identifier}' OR phone='{identifier}'")
    conn.commit()
    conn.close()
