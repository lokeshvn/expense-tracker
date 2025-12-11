import tkinter as tk
from tkinter import messagebox
from services.expenses import add_expense, list_expenses


def refresh_listbox():
    listbox.delete(0, tk.END)
    rows = list_expenses()
    for row in rows:
        row_id, amount, category, date, note = row
        listbox.insert(tk.END, f"{row_id} | {date} | {category} | {amount} | {note}")


def on_add_click():
    try:
        amount_value = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return

    category_value = category_entry.get().strip()
    date_value = date_entry.get().strip()
    note_value = note_entry.get().strip()

    try:
        add_expense(amount_value, category_value, date_value, note_value)
        messagebox.showinfo("Success", "Expense added")
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        note_entry.delete(0, tk.END)
        refresh_listbox()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# main window
root = tk.Tk()
root.title("Expense Tracker - Simple")

# amount
tk.Label(root, text="Amount").grid(row=0, column=0, padx=5, pady=5, sticky="e")
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

# category
tk.Label(root, text="Category").grid(row=1, column=0, padx=5, pady=5, sticky="e")
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1, padx=5, pady=5)

# date
tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=2, column=0, padx=5, pady=5, sticky="e")
date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1, padx=5, pady=5)

# note
tk.Label(root, text="Note").grid(row=3, column=0, padx=5, pady=5, sticky="e")
note_entry = tk.Entry(root)
note_entry.grid(row=3, column=1, padx=5, pady=5)

# add button
add_button = tk.Button(root, text="Add Expense", command=on_add_click)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

# listbox
listbox = tk.Listbox(root, width=60)
listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# load existing data
refresh_listbox()

root.mainloop()
