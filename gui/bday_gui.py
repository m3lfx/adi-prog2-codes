import tkinter as tk
import tkinter.messagebox

birthdays = {}

def main():
    global name_entry, bday_entry

    root = tk.Tk()
    root.geometry("400x400")
    root.title("Employee Form")

    tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=10, pady=5) 

    tk.Label(root, text="Birthday:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
    bday_entry = tk.Entry(root) 
    bday_entry.grid(row=1, column=1, padx=10, pady=5)

    create_btn = tk.Button(root, text="Add", command=lambda: create(name_entry.get(), bday_entry.get()))
    create_btn.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()

def create(name, bday):
    print(name, bday)
    
    if name not in birthdays:
        birthdays[name] = bday
        print(birthdays)
    else:
        tk.messagebox.showwarning('warning', 'name already exist')
    
    bday_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    name_entry.focus_set()

main()