def main():
    # Create a list of strings.
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas', 'houston', 'gentri']
     # Open a file for writing.
    outfile = open('cities.txt', 'w')

    # Write the list to the file.
    # outfile.writelines(cities)

    for item in cities:
        # outfile.write(item + '\n')
        outfile.write(f"{item}\t")


    # Close the file.
    outfile.close()

# Call the main function.
main()
