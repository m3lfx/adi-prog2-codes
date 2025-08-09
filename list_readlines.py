def main():
    # Open a file for reading.

    infile = open('cities.txt', 'r')
    # Read the contents of the file into a list.
    cities = infile.readlines()
    print(cities)

    # Close the file.
    infile.close()

    # # Strip the \n from each element.
    index = 0
    # while index < len(cities):
    #     cities[index] = cities[index].rstrip('\n')
    #     index +=1
    
    for city in cities:
        temp_city = city.rstrip('\n')
        
        #remove third character
        cities[index] = temp_city[:2] + temp_city[3:]
        index +=1

    # Print the contents of the list.
    print(cities)

    my_string = 'Roses are red'
    print(my_string[2])

# Call the main function.
main()