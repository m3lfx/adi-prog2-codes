def main():
    # Get a list with values stored in it.
    numbers = get_values()
    # Display the values in the list.
    print('The numbers in the list are:')
    print(numbers)

def get_values():
    # Create an empty list.
    values = []
    again = 'y'

# Get values from the user and add them to the list.
    while again == 'y':
        # Get a number and add it to the list.
        num = int(input('Enter a number: '))
        values.append(num)

        # Want to do this again?
        print('Do you want to add another number?')
        again = input('y = yes, anything else = no: ')
        print()

    # Return the list 
    return values

# Call the main function.
main()
