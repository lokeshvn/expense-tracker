import sqlite3
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "expenses.db"


def load_expenses_df():
    """Return all expenses as a Pandas DataFrame."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()
    return df


def show_category_bar_chart():
    """Show total amount per category as a bar chart."""
    df = load_expenses_df()
    if df.empty:
        print("No data to plot.")
        return

    grouped = df.groupby("category")["amount"].sum()

    plt.figure(figsize=(6, 4))
    grouped.plot(kind="bar")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.title("Expenses by Category")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    show_category_bar_chart()
