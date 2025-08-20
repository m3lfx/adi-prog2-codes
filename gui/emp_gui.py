import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry, Calendar
import customtkinter as ctk
import csv
import os

FILE_NAME = "emp.csv"

def main():
    global id_num_entry, first_name_entry, last_name_entry, dept_entry, id_num_entry, cal, position_entry

    # root = tk.Tk()
    root = ctk.CTk()
    root.geometry("400x400")
    root.title("Employee Form")

    tk.Label(root, text="ID number:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
    id_num_entry = tk.Entry(root)
    id_num_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="First Name:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
    first_name_entry = tk.Entry(root)
    first_name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Last Name:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
    last_name_entry = tk.Entry(root)
    last_name_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Position:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
    position_entry = tk.Entry(root)
    position_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Department:").grid(row=4, column=0, padx=10, pady=5, sticky='e')
    dept_entry = tk.Entry(root)
    dept_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(root, text="Date of Hire:").grid(row=5, column=0, padx=10, pady=5, sticky='e')
    # cal = DateEntry(root, width=15, background='darkblue', cursor="hand1", foreground='white', date_pattern='yyyy-mm-dd', selectmode = 'day', )
    cal = Calendar(root, selectmode = 'day', date_pattern='yyyy-mm-dd', )
    cal.grid(row=5, column=1, padx=10, pady=5)
    
    submit_btn = tk.Button(root, text="Submit", command=submit)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=15)

    table_btn = tk.Button(root, text="Show Table", command=lambda: show_table(FILE_NAME))
    table_btn.grid(row=7, column=0, columnspan=2, pady=10)
   
    

    root.mainloop()

def submit():
    id = id_num_entry.get()
    first = first_name_entry.get()
    last = last_name_entry.get()
    position = position_entry.get()
    dept = dept_entry.get()
    date = cal.get_date()

    save_emp(FILE_NAME, id, first, last, position, dept, date)
    clear()


def save_emp(filename, id, first_name, last_name, position, department,date_hired):
    emp_data = [id, first_name, last_name, position, department, date_hired]
    header = ['ID', 'first_name', 'last_name', 'position', 'department', 'date_hired']

    if os.path.exists(filename):
        if os.path.getsize(filename) > 0:
            emp_file = open(filename, 'a', newline='')
    
    else:
        emp_file = open(filename, 'w', newline='')
        emp_file.write(" ".join(header) + "\n")
    
    writer = csv.writer(emp_file)
    writer.writerow(emp_data)
    emp_file.close()
        
def show_table(filename):
    # Create a new window for the table
    table_window = ctk.CTkToplevel()
    table_window.title("Employee Table")

    # Create a Treeview widget
    tree = ttk.Treeview(table_window, show="headings", )
    tree.pack(padx=10, pady=10, expand=True, fill='both')

    # Read the CSV file
    csvfile = open(filename, 'r', newline='')

    reader = csv.reader(csvfile)

    rows = list(reader)
    print(rows)
    header = rows[0][0].split()
    
    print(header)

    if not rows:
        return
    
    tree["columns"] = header

    for col in header:
        # print(col)
        tree.heading(col, text=col)
        # tree.column(col, width=200)
        tree.column(col, anchor=tk.CENTER)

    for row in rows[1:]:
        print(row)
        tree.insert("", tk.END, values=row)
    
    csvfile.close()

def clear():
    id_num_entry.delete(0, tk.END)
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    position_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END) 
    cal.selection_clear()

main()