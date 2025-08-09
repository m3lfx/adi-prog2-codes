filename = input('Enter the filename: ')
if filename.endswith('.txt'):
        print('That is the name of a text file.')
elif filename.endswith('.py'):
    print('That is the name of a Python source file.')
elif filename.endswith('.doc'):
    print('That is the name of a word processing document.')
else:
    print('Unknown file type.')


string = 'Four score and seven years ago'
position = string.find('score')
if position != -1:
    print('The word "score" was found at index', position)
else:
    print('The word "seven" was not found.')

string = 'F0ur fack you and seven years ago. years in 2025 years'
new_string = string.replace('duck', '****')
print(new_string)
