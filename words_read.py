def main():

    num_words = 0
    ave_wordlength = 0
    total_length = 0
    long_word = ""
    word_list = []
    len_word = []

    word_file = open('words.txt', 'r')
    line = word_file.readline()

    while line != '':
        num_words += 1
        print(line)
        word_list.append(line.rstrip('\n'))
        total_length += len(line.rstrip('\n'))
        line = word_file.readline()

    for word in word_list:
        len_word.append(len(word))

    long_word = max(len_word)
      
    ave_wordlength = total_length / num_words
    print(f"total number of words in the file {num_words}")
    print(f"average length of words in file {ave_wordlength}")
    print(f"the longest word is {long_word} ")
main()