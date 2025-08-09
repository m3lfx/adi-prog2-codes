def main():
    # Create a list of numbers.
    numbers = [1, 2, 3, 4, 5, 6, 7]

    # Open a file for writing.
    outfile = open('numberlist.txt', 'w')

    for number in numbers:
        # outfile.write(str(number) + '\n')
        outfile.write(f"{number}\n")

    # Close the file.
    outfile.close()

# Call the main function.
main()