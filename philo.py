def main():
    # Open a file named philosophers.txt.
    outfile = open('philosophers.txt', 'a')

    # Write the names of three philosphers to the file.
    outfile.write('andrew e\n')
    outfile.write('hayden kho\n')
    outfile.write('meme vice\n')

    # Close the file.
    outfile.close()

# Call the main function.
main()