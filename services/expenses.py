from db.db import get_connection, init_db


def add_expense(amount, category, date, note=""):
    """Insert one expense row into the database."""
    # basic validation
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if not category:
        raise ValueError("Category is required")
    if not date:
        raise ValueError("Date is required (e.g. 2025-12-11)")

    init_db()  # make sure table exists
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO expenses (amount, category, date, note)
        VALUES (?, ?, ?, ?)
        """,
        (amount, category, date, note),
    )

    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def list_expenses():
    """Return all expenses as a list of tuples."""
    init_db()
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, amount, category, date, note FROM expenses")
    rows = cur.fetchall()

    conn.close()
    return rows


if __name__ == "__main__":
    # quick manual test
    expense_id = add_expense(100, "Food", "2025-12-11", "Lunch")
    print("Inserted id:", expense_id)
    print("All rows:")
    for row in list_expenses():
        print(row)
