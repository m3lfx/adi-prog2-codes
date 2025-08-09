def main():
    num_words = int(input("enter number of words"))
    outfile = open('words.txt', 'a')
    for i in range(num_words):
        words = input("enter words")
        outfile.write(f"{words}\n")

main()