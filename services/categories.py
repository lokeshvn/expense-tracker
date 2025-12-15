from db.db import get_connection, init_db


def add_category(name: str):
    name = name.strip()
    if not name:
        return
    init_db()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()


def list_categories():
    init_db()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM categories ORDER BY name")
    rows = [r[0] for r in cur.fetchall()]
    conn.close()
    return rows
