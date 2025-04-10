# Python implementation to compute
# number of characters, words, spaces
# and lines in a file

# Function to count number
# of characters, words, spaces
# and lines in a file
def counter(fname):
    # variable to store total word count
    num_words = 0

    # variable to store total line count
    num_lines = 0

    # variable to store total character count
    num_charc = 0

    # variable to store total space count
    num_spaces = 0

    # opening file using with() method
    # so that file gets closed
    # after completion of work
    with open(fname, 'r') as f:
        for line in f:
            num_lines += 1
            word = 'Y'
            for letter in line:
                if (letter != ' ' and word == 'Y'):
                    num_words += 1
                    word = 'N'
                elif (letter == ' '):
                    num_spaces += 1

                    word = 'Y'
                for i in letter:

                    if (i != " " and i != "\n"):
                        # incrementing character
                        # count by 1
                        num_charc += 1

    # printing total word count
    print("Number of words in text file: ", num_words)

    # printing total line count
    print("Number of lines in text file: ", num_lines)

    # printing total character count
    print('Number of characters in text file: ', num_charc)

    # printing total space count
    print('Number of spaces in text file: ', num_spaces)


# Driver Code:
if __name__ == '__main__':
    fname = 'File1.txt'
    try:
        counter(fname)
    except:
        print('File not found')