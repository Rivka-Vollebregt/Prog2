################################################################################
# greedy.py
#
# Programmeren 2
#
# Rivka Vollebregt
# 12164968
#
# Calculates the minimal number of coins that a certain amount of
# change requires. The user is prompted for the amount of change

from cs50 import get_float


def main():

    # ask user for the amount of change owed
    amount = get_dollars("change owed: $ ")

    # counter to track number of coins used for change
    counter = 0

    # different coins available for change
    coins = {25, 10, 5, 1}

    for coin in coins:
        amount %= coin

        counter += 1

    # output of program: print the minimal number of coins necessary
    print(counter)


# function to prompt user till amount of change is given
def get_dollars(prompt):
    while True:
        dollars = get_float("change owed: $ ")
        dollars *= 100
        amount = round(dollars)
        if amount > 0:
            break
    return amount


if __name__ == "__main__":
    main()