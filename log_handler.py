import sqlite3
import datetime

def add_call_log(number, timestamp=None):
    if not timestamp:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect("database/call_forwarding.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO call_logs (number, timestamp)
        VALUES (?, ?)
    """, (number, timestamp))
    conn.commit()
    conn.close()