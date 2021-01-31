################################################################################
# bleep.py
#
# Programmeren 2
#
# Rivka Vollebregt
# 12164968
#
# Checks a message given by user, checks it for curse words
# and returns it with the curse words censored


from cs50 import get_string
import sys


def main():

    # check if command line argument is present and < 2, if not -> error
    if len(sys.argv) != 2:
        print("Error, missing command-line argument")
        exit(1)

    # save file specified in command line argument as inputfile
    #inputfile = sys.argv[1]

    # open command line argument file with banned words
    infile = open(sys.argv[1], 'r')
    library = []

    # put every banned word in the list: library
    for line in infile:
        word = infile.readline()
        library.append(line[:-1])
        library.append(word[:-1])

    # get message from the user
    text = get_string("What message would you like to censor?\n")
    message_lower = text.lower().split()

    # split message into different words
    message = text.split()

    # iterating over library
    for i in range(len(library)):

        # iterating over words in the message
        for j in range(len(message)):

            if library[i] == message_lower[j]:

                # create variable copy_message to store bleeped word
                copy_message = ""

                # create word consisting of * with length of original word
                for i in range(len(message[j])):
                    copy_message = copy_message + '*'

                # copy censored word into message
                message[j] = copy_message

    # print message containing the censored words
    censored = " ".join(map(str, message))
    print(censored)


if __name__ == "__main__":
    main()
