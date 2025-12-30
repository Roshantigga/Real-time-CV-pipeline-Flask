import sqlite3

def init_db():
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            event_type TEXT,
            value REAL
        )
    """)
    conn.commit()
    conn.close()

def insert_event(event):
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO events (timestamp, event_type, value) VALUES (?, ?, ?)",
        (event["timestamp"], event["event_type"], event["value"])
    )
    conn.commit()
    conn.close()

init_db()

