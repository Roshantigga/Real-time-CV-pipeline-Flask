import sqlite3

conn = sqlite3.connect("events.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM events")
for row in cursor.fetchall():
    print(row)

conn.close()
