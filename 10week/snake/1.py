
import psycopg2

conn = psycopg2.connect("dbname=snake user=aisha password=30121995")
cur = conn.cursor()

name = input("Введите имя пользователя: ")

cur.execute("INSERT INTO user (name) VALUES (%s) ON CONFLICT DO NOTHING", (name,))
conn.commit()

#Запрос на вывод текущего уровня пользователя
cur.execute("SELECT level FROM user_score WHERE user_id = (SELECT id FROM user WHERE name = %s)", (name,))
result = cur.fetchone()

if result:
   print(f"Текущий уровень пользователя {name}: {result[0]}")
else:
   print("Новый пользователь")

#Перед началом игры сохраняем состояние и оценку пользователя
level = input("Введите уровень: ")
score = input("Введите количество очков: ")

cur.execute("INSERT INTO user_score (user_id, level, score) VALUES ((SELECT id FROM user WHERE name = %s), %s, %s)", (name, level, score))
conn.commit()

#После игры обновляем оценку пользователя
new_score = input("Введите новое количество очков: ")

cur.execute("UPDATE user_score SET score = %s WHERE user_id = (SELECT id FROM user WHERE name = %s)", (new_score, name))
conn.commit()

cur.close()
conn.close()