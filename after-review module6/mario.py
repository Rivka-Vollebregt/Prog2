################################################################################
# mario.py
#
# Programmeren 2
#
# Rivka Vollebregt
# 12164968
#
# Creates two pyramids, one left and one right with the height that
# the user enters when prompted


from cs50 import get_int


def main():

    # function that prompts user until a positive integer is given
    while True:
        height = get_int("Height: ")
        if height >= 0 and height <= 23:
            break

    for row in range(height):

        # prints spaces of left pyramid
        print(" " * (height - row - 1), end='')

        # prints hashes of left pyramid
        print("#" * (row + 1), end='')

        # prints two middle spaces
        print("  ", end='')

        # prints hashes of right pyramid
        print("#" * (row + 1), end='')

        print()


if __name__ == "__main__":
    main()
