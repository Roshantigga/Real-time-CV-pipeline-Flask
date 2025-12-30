import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "events.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
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
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO events (timestamp, event_type, value) VALUES (?, ?, ?)",
        (event["timestamp"], event["event_type"], event["value"])
    )
    conn.commit()
    conn.close()

# MUST run on import
init_db()
