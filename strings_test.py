name = 'Juliet'
for ch in name:
    print(ch)

def main():
    # Create a variable to use to hold the count. The variable must start with 0.
    count = 0

    # Get a string from the user.
    # my_string = input('Enter a sentence: ')

    # Count the Ts.
    # for ch in my_string:
    #     if ch == 'T' or ch == 't':
    #         count += 1

    # Print the result.
    # print('The letter T appears', count, 'times.')
    my_string = 'Roses are red'
    print(my_string[0], my_string[6], my_string[10])

    city = 'Boston'
    size = len(city)
    print(size)

    first_name = 'Emily'
    last_name = 'Yeager'
    full_name = first_name + ' ' + last_name
    print(full_name)

    letters = 'abc'
    letters += 'def'
    print(letters)

    # name = 'Carmen'
    # print('The name is', name)
    # name = name + ' Brown'
    # print('Now the name is', name)

    full_name = 'Patty Lynn Smith'
    middle_name = full_name[6:10]
    print(middle_name)

    full_name = 'Patty Lynn Smith'
    first_name = full_name[:5]
    print(first_name)

    full_name = 'Patty Lynn Smith jr'
    last_name = full_name[11:]
    print(last_name)

    full_name = 'Patty Lynn Smith'
    last_name = full_name[-5:]
    print(last_name)

    text = 'Four score and seven years ago'
    if 'Seven' not in text:
        print('The string "seven" was found.')
    else:
        print('The string "seven" was not found.')
    

    string1 = 'abcde34'
    if string1.isalnum():
        print(string1, 'contains only alpha numeric.')
    else:
        print(string1, 'contains characters other than digits.')

# # Call the main function.

    date_string = '11/26/2018'
    date_list = date_string.split('/')
    print(date_list)
main()
