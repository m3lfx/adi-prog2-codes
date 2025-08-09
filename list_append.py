def main():
    # First, create an empty list.
    name_list = []

    # Create a variable to control the loop.
    again = 'y'

    # Add some names to the list.
    while again == 'y':
        # Get a name from the user.
        name = input('Enter a name: ')
        name_list.append(name)
        # Add another one?
        print('Do you want to add another name?')
        again = input('y = yes, anything else = no: ')
        print()
        print(name_list)

        print('Here are the names you entered.')

    for name in name_list:
        print(name)

# Call the main function.
main()