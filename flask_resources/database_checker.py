import sqlite3

conn = sqlite3.connect('instance\\resources.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM resource')
cursor.execute('SELECT * FROM mood_log')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()