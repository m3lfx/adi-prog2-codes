def main():
    # Create a bool variable to use as a flag.
    found = False

     # Get the search value.
    search = input('Enter a description to search for: ')

     # Open the coffee.txt file.
    coffee_file = open('coffee.txt', 'r')

    # Read the first record's description field.
    descr = coffee_file.readline()

    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        if descr == search.lower():
            # Display the record.
            print('Description:', descr)
            print('Quantity:', qty)
            print()
            # Set the found flag to True.
            found = True
        # Read the next description.
        descr = coffee_file.readline()

    # Close the file.
    coffee_file.close()

    if not found:
        print('That item was not found in the file.')


main()