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

    update_btn = tk.Button(root, text="update", command=lambda: update(name_entry.get(), bday_entry.get()))
    update_btn.grid(row=3, column=0, columnspan=2, pady=10)

    delete_btn = tk.Button(root, text="delete", command=lambda: delete(name_entry.get()))
    delete_btn.grid(row=4, column=0, columnspan=2, pady=10)
    

    root.mainloop()

def create(name, bday):
    print(name, bday)
    
    if name not in birthdays:
        birthdays[name] = bday
        print(birthdays)
    else:
        tk.messagebox.showwarning('warning', 'name already exist')
    
    clear()


def update(name, bday):
    if name in birthdays:
        birthdays[name] = bday
        tk.messagebox.showinfo('success', 'birthday updated')
    else:
        tk.messagebox.showwarning('warning', 'name not found')
    
    print(birthdays)
    clear()


def delete(name):

    if name in birthdays:
        response = tk.messagebox.askyesnocancel(
        "Delete Confirmation",
        "Are you sure you want to delete this friend")
        print(response)

        if response is True:
            
            del birthdays[name]
            tk.messagebox.showinfo('warning', 'name record deleted')
        
        elif response is False:
            tk.messagebox.showinfo('warning', 'no response')

        else:  # response is None
             tk.messagebox.showinfo('warning', 'thank you')

    print(birthdays)



def clear():
    bday_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    name_entry.focus_set()
main()