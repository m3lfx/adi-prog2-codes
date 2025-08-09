def main():
    word_file = open('words.txt', 'r')
    line = word_file.readline()

    num_words = 0
    ave_wordlength = 0
    total_length = 0
    long_word = ""
    while line != '':
        long_word = line
        num_words += 1
        print(line)
        total_length += len(line.rstrip('\n'))
        line = word_file.readline()

        if len(long_word) < len(line):
            long_word = line

    ave_wordlength = total_length / num_words
    print(f"total number of words in the file {num_words}")
    print(f"average length of words in file {ave_wordlength}")
    print(f"the longest word is {long_word} {len(long_word)}")
main()