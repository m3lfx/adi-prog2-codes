def main():
    # Open a file for writing.
    outfile = open('numbers.txt', 'a')

    # Get three numbers from the user.
    num1 = float(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    num3 = int(input('Enter another number: '))

    # Write the numbers to the file.
    outfile.write(f"{num1} \n")
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')
    # outfile.write(num1)
    # outfile.write(num2)
    # outfile.write(num3)

    # Close the file.
    outfile.close()
    print('Data written to numbers.txt')

# Call the main function.
main()