import psycopg2

def get_data_with_pagination(table_name, limit, offset):
    conn = psycopg2.connect(database="phonebook1", user="aisha", password="30121995")
    cur = conn.cursor()
    query = f"SELECT * FROM {table_name} LIMIT {limit} OFFSET {offset}"
    cur.execute(query)
    data = cur.fetchall()
    conn.close()
    return data
