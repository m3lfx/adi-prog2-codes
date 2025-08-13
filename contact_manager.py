import contact
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
LIST = 5
QUIT = 6

FILENAME = 'contacts.dat'

def main():
    # Load the existing contact dictionary and assign it to mycontacts.
   
    mycontacts = load_contacts()
    # Initialize a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == LIST:
            list_contacts(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)
        

    # Save the mycontacts dictionary to a file.
    save_contacts(mycontacts)

def load_contacts():
    try:
        # Open the contacts.dat file.
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        contact_dct = pickle.load(input_file)

        # Close the phone_inventory.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create # an empty dictionary.
        contact_dct = {}

    # Return the dictionary.
    return contact_dct

def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up a contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact')
    print('5. Contact List')
    print('6. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))
    

    # Validate the choice.
   
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

def look_up(mycontacts):
    # Get a name to look up.
    name = input('Enter a name: ')

    # Look it up in the dictionary.
    
    print(mycontacts.get(name, 'That name is not found.'))



# The add function adds a new entry into the specified dictionary.
def add(mycontacts):
    # Get the contact info.
    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')

    # Create a Contact object named entry.
    entry = contact.Contact(name, phone, email)

    # If the name does not exist in the dictionary, add it as a key with the entry object as the associated value.
    if name not in mycontacts:
        mycontacts[name] = entry
        print('The entry has been added.')
    else:
        print('That name already exists.')

def change(mycontacts):
    # Get a name to look up.
    name = input('Enter a name: ')

    if name in mycontacts:
        # Get a new phone number.
        phone = input('Enter the new phone number: ')

        # Get a new email address.
        email = input('Enter the new email address: ')

        # Create a contact object named entry.
        entry = contact.Contact(name, phone, email)

        # Update the entry.
        mycontacts[name] = entry
        print('Information updated.')
    else:
        print('That name is not found.')


def delete(mycontacts):
    # Get a name to look up.
    name = input('Enter a name: ')

    # If the name is found, delete the entry.
    if name in mycontacts:
        del mycontacts[name]
        print('Entry deleted.')
    else:
        print('That name is not found.')

def save_contacts(mycontacts):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(mycontacts, output_file)

    # Close the file.
    output_file.close()

def list_contacts(mycontacts):
    # print(mycontacts.items())
    for key, value in mycontacts.items():
        print(value)
        print(f"Contact {key} data: {value}")
        print() 

main()