import psycopg2

def insert_many_users(user_list):
    conn = psycopg2.connect(database="phonebook1", user="aisha", password="30121995")
    cur = conn.cursor()
    for user in user_list:
        name, phone = user[0], user[1]
        if len(phone) != 10:
            cur.execute("INSERT INTO IncorrectData (first_name, phone) VALUES (%s, %s)", (name, phone))
        else:
            cur.execute("INSERT INTO contacts (first_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    conn.close()
