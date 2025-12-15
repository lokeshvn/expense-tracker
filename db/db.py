import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "expenses.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            note TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS categories (
            name TEXT PRIMARY KEY
        )
        """
         )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database and table ready.")
