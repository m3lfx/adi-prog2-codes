def main():
    num_golfers = int(input('How many golfer records do you want to create? '))

    # Open a file for writing.
    golf_file = open('golf.txt', 'w')

    for count in range(1, num_golfers + 1):
        # Get the data for an employee.
        print('Enter data for golfer #', count, sep='')
        name = input('Name: ')
        score = input('Score: ')

        golf_file.write(name + '\n')
        golf_file.write(score + '\n')
    golf_file.close()
    read_golfers()

def read_golfers():
    golf_file = open('golf.txt', 'r')

    # Read the first line from the file, which is
    # the name field of the first record.
    name = golf_file.readline()

    # If a field was read, continue processing.
    while name != '':
        # Read the ID number field.
        score = golf_file.readline()
        print(f"Name:, {name.rstrip('\n')}")
        print(f"score:, {score.rstrip('\n')}")
        name = golf_file.readline()
    golf_file.close()
    
main()