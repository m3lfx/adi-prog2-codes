import contact
import pickle
import tkinter as tk
from tkinter  import messagebox

FILENAME = 'contacts.dat'

def main():
    global name_entry, email_entry, phone_entry

    mycontacts = load_contacts(FILENAME)
    print(mycontacts)

    root = tk.Tk()
    root.geometry("400x400")
    root.title("Contact Form")

    tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
    name_entry = tk.Entry(root) 
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
    email_entry = tk.Entry(root) 
    email_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Phone:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
    phone_entry = tk.Entry(root) 
    phone_entry.grid(row=2, column=1, padx=10, pady=5)

    create_btn = tk.Button(root, text="Save Contact", command=lambda: create(name_entry.get(), email_entry.get(), phone_entry.get(), mycontacts))
    create_btn.grid(row=3, column=0, columnspan=2, pady=10)

    update_btn = tk.Button(root, text="Update Contact", command=lambda: change(mycontacts, name_entry.get(), email_entry.get(), phone_entry.get(), ))
    update_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    delete_btn = tk.Button(root, text="Delete Contact", command=lambda: delete(mycontacts, name_entry.get() ))
    delete_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

def create(name, email, phone, contacts):

    entry = contact.Contact(name, phone, email)
    print(entry)
    if name not in contacts:
        contacts[name] = entry
        tk.messagebox.showinfo('Response', 'Contact Added')
        clear_form()
    else:
        tk.messagebox.showinfo('Response', 'Name already exists')
        clear_form()
    
    save_contacts(contacts, FILENAME) 

def load_contacts(filename):
    try:
        # Open the contacts.dat file.
        print(filename)
        input_file = open(filename, 'rb')

        # Unpickle the dictionary.
        contact_dct = pickle.load(input_file)
        print(contact_dct)

        # Close the phone_inventory.dat file.
        input_file.close()

    except IOError:
        # Could not open the file, so create # an empty dictionary.
        contact_dct = {}

    # Return the dictionary.
    return contact_dct


def save_contacts(mycontacts, filename):
    # Open the file for writing.
    output_file = open(filename, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(mycontacts, output_file)

    # Close the file.
    output_file.close()

def change(mycontacts, name, email, phone):
    if name in mycontacts:
        
        # Create a contact object named entry.
        entry = contact.Contact(name, phone, email)

        # Update the entry.
        mycontacts[name] = entry
        print('Information updated.')
        tk.messagebox.showinfo('Response', 'Contact Updated')
        clear_form()
    else:
        tk.messagebox.showinfo('Response', 'Name not found')
        clear_form()


def delete(mycontacts, name):

    if name in mycontacts:
        response = tk.messagebox.askyesnocancel(
        "Delete Confirmation",
        "Are you sure you want to delete this contact")
        
        if response is True:
            print("User clicked Yes - Proceeding with deletion.")
            del mycontacts[name]
            # Add your deletion logic here
        elif response is False:
            print("User clicked No - Deletion cancelled.")
        else:  # response is None
            print("User clicked Cancel - Operation aborted.")
    else:
        tk.messagebox.showinfo('warning', 'name not found')
    
    print(mycontacts)
def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

main()

