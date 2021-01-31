################################################################################
# viginere.py
#
# Programmeren 2
#
# Rivka Vollebregt
# 12164968
#
# viginere encripton function encrypts plaintext given as input by the user
# the encription key is the command line argument.
# plaintext entered by user is shifted using the value of encription key


import sys
from cs50 import get_string


def main():

    # check if command line argument is present and < 2, if not -> error
    if len(sys.argv) != 2:
        print("Error, missing command-line argument")
        exit(1)

    # check if command line argument is all letters
    if sys.argv[1].isalpha() == False:
        print("Enter only letters")
        exit(1)

    # prompt user for string plaintext
    plaintext = get_string("plaintext: ")

    # print "ciphertext:" , after which ciphertext characters will be printed
    print("ciphertext: ", end="")

    # track position in the key
    key_position = 0
    key_length = len(sys.argv[1])

    # go through every character in plaintext to encript if it's a letter
    for c in plaintext:

        if c.isalpha():

            # convert key character to lowercase
            key = ord(sys.argv[1][key_position % key_length].lower()) - 97        ####key apart definen
            key_position += 1

            # encrypt c using key, keep case in encripted letter
            if c.isupper():
                ciphertext = chr(((ord(c) - 65 + key) % 26) + 65)
            else:
                ciphertext = chr(((ord(c) - 97 + key) % 26) + 97)

        # if character is not letter, save in ciphertext without encripting
        else:
            ciphertext = c

        # print ciphertext
        print(f"{ciphertext}", end="")

    print()


if __name__ == "__main__":
    main()