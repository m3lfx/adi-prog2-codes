LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
# Create an empty dictionary.

    birthdays = {}
    # Initialize a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)
    
    

 # The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('Friends and Their Birthdays')
    print('---------------------------')
    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit the program')
    print()
    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

def look_up(birthdays):
    # Get a name to look up.
    name = input('Enter a name: ')
    # Look it up in the dictionary.
    print(birthdays.get(name, 'Not found.'))

def add(birthdays):
    # Get a name and birthday.
    name = input('Enter a name: ')
    bday = input('Enter a birthday: ')

    # If the name does not exist, add it.
    if name not in birthdays:
        birthdays[name] = bday
    else:
        print('That entry already exists.')
    
    print(birthdays)

def change(birthdays):
    # Get a name to look up.
    name = input('Enter a name: ')

    if name in birthdays:
        # Get a new birthday.
        bday = input('Enter the new birthday: ')

        # Update the entry.
        birthdays[name] = bday
    else:
        print('That name is not found.')

def delete(birthdays):
    # Get a name to look up.
    name = input('Enter a name: ')
    # If the name is found, delete the entry.
    if name in birthdays:
        del birthdays[name]
    else:
        print('That name is not found.')

# Call the main function.
main()


