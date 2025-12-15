import tkinter as tk
from tkinter import messagebox
from services.expenses import add_expense, list_expenses, update_expense, delete_expense

from services.reports import show_category_bar_chart

from tkinter import messagebox, ttk
from services.categories import add_category , list_categories




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

    # category_value = category_entry.get().strip()
    category_value = category_combobox.get().strip()

    date_value = date_entry.get().strip()
    note_value = note_entry.get().strip()

    try:
        add_expense(amount_value, category_value, date_value, note_value)
        messagebox.showinfo("Success", "Expense added")
        amount_entry.delete(0, tk.END)
        category_combobox.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        note_entry.delete(0, tk.END)
        refresh_listbox()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# main window
root = tk.Tk()
selected_id = None

root.title("Expense Tracker - Simple")

# amount
tk.Label(root, text="Amount").grid(row=0, column=0, padx=5, pady=5, sticky="e")
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

# category
# tk.Label(root, text="Category").grid(row=1, column=0, padx=5, pady=5, sticky="e")
# category_entry = tk.Entry(root)
# category_entry.grid(row=1, column=1, padx=5, pady=5)


def load_categories_into_combobox():
    categories = list_categories()
    category_combobox["values"] = categories

# label same as before
tk.Label(root, text="Category").grid(row=1, column=0, padx=5, pady=5, sticky="e")
category_combobox = ttk.Combobox(root)
category_combobox.grid(row=1, column=1, padx=5, pady=5)
load_categories_into_combobox()


def on_add_category_click():
    new_cat = category_combobox.get().strip()
    if not new_cat:
        messagebox.showerror("Error", "Type category name in box first")
        return
    add_category(new_cat)
    load_categories_into_combobox()
    messagebox.showinfo("Success", "Category added")


add_cat_button = tk.Button(root, text="Add Category", command=on_add_category_click)
add_cat_button.grid(row=1, column=2, padx=5, pady=5)



# date
tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=2, column=0, padx=5, pady=5, sticky="e")
date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1, padx=5, pady=5)

# note
tk.Label(root, text="Note").grid(row=3, column=0, padx=5, pady=5, sticky="e")
note_entry = tk.Entry(root)
note_entry.grid(row=3, column=1, padx=5, pady=5)

# add button
# add_button = tk.Button(root, text="Add Expense", command=on_add_click)
# add_button.grid(row=4, column=0, columnspan=2, pady=10)

def on_update_click():
    if selected_id is None:
        messagebox.showerror("Error", "Select a row to update")
        return
    try:
        amount_value = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return

    # category_value = category_entry.get().strip()
    category_value = category_combobox.get().strip()


    date_value = date_entry.get().strip()
    note_value = note_entry.get().strip()

    try:
        update_expense(selected_id, amount_value, category_value, date_value, note_value)
        messagebox.showinfo("Success", "Expense updated")
        refresh_listbox()
        # clear fields
        amount_entry.delete(0, tk.END)
        category_combobox.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        note_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def on_delete_click():
    if selected_id is None:
        messagebox.showerror("Error", "Select a row to delete")
        return
    try:
        delete_expense(selected_id)
        messagebox.showinfo("Success", "Expense deleted")
        # clear fields
        amount_entry.delete(0, tk.END)
        category_combobox.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        note_entry.delete(0, tk.END)
        refresh_listbox()
    except Exception as e:
        messagebox.showerror("Error", str(e))

add_button = tk.Button(root, text="Add Expense", command=on_add_click)
add_button.grid(row=4, column=0, pady=10)

update_button = tk.Button(root, text="Update", command=on_update_click)
update_button.grid(row=4, column=1, pady=10)

delete_button = tk.Button(root, text="Delete", command=on_delete_click)
delete_button.grid(row=4, column=2, padx=5, pady=10)



report_button = tk.Button(root, text="Show Category Report", command=show_category_bar_chart)
report_button.grid(row=4, column=3, padx=5, pady=10)


# listbox
listbox = tk.Listbox(root, width=60)
listbox.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

def on_listbox_select(event):
    global selected_id
    selection = listbox.curselection()
    if not selection:
        selected_id = None
        return
    index = selection[0]
    value = listbox.get(index)
    # value format: "id | date | category | amount | note"
    parts = [p.strip() for p in value.split("|")]
    if len(parts) >= 5:
        selected_id = int(parts[0])
        date_entry.delete(0, tk.END)
        date_entry.insert(0, parts[1])

        category_combobox.delete(0, tk.END)
        category_combobox.insert(0, parts[2])


        amount_entry.delete(0, tk.END)
        amount_entry.insert(0, parts[3])

        note_entry.delete(0, tk.END)
        note_entry.insert(0, parts[4])


listbox.bind("<<ListboxSelect>>", on_listbox_select)


# load existing data
refresh_listbox()

root.mainloop()
