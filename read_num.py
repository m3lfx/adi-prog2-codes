def main():
    # Open a file for reading.
    infile = open('numbers.txt', 'r')

    # Read three numbers from the file.
    # num1 = float(infile.readline())
    # num2 = int(infile.readline())
    # num3 = int(infile.readline())

    num1 = infile.readline()
    num2 = infile.readline()
    num3 = infile.readline()

    # Close the file.
    infile.close()

    # Add the three numbers.
    total = num1 + num2 + num3

    # Display the numbers and their total.
    print('The numbers are:', num1, num2, num3)
    print('Their total is:', total)

    # Call the main function.
main()