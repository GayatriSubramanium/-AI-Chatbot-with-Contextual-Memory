import sqlite3
from datetime import datetime

# Connect to the database (or create it)
conn = sqlite3.connect("chat_logs.db", check_same_thread=False)
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        user TEXT,
        role TEXT,
        message TEXT
    )
""")
conn.commit()

def log_message(user, role, message):
    timestamp = datetime.now().isoformat()
    cursor.execute("INSERT INTO logs (timestamp, user, role, message) VALUES (?, ?, ?, ?)",
                   (timestamp, user, role, message))
    conn.commit()
