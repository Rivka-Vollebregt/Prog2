################################################################################
# hangman.py
#
# Programmeren 2
#
# Rivka Vollebregt
# 12164968
#
# Allows user to play a game of hangman


import random


class Lexicon:

    def __init__(self):
        self.words = []
        # Load the dictionary of words.
        file = open('dictionary.txt', 'r')
        # put words in list
        for line in file:
            line = line.strip()
            self.words.append(line)

        # print the number of words loaded in list
        print("  ", len(self.words), "words loaded.")

    def get_words(self, length):
        # Return a list of all words from the dictionary of the given length.
        # create new list
        self.correctlength_list = []

        # add words of correct length in correctlength_list
        for word in self.words:
            word = word.strip().lower()
            if len(word) == length:
                self.correctlength_list.append(word)
        return self.correctlength_list

    def get_word(self, length):
        # Return a single random word of given length. Uses `get_words` above.
        return random.choice(self.get_words(length))


class Hangman:
    def __init__(self, length, num_guesses):
        # Initialize game by choosing a word and creating an empty pattern.
        self.length = length
        self.num_guesses = num_guesses

        # assertions for length of word and guesses
        assert length > 1 and length < 29
        assert num_guesses > 1 and num_guesses < 27

        l = Lexicon()
        stringword = l.get_word(length)
        self.misteryword = []
        # store chosen word in misteryword
        for char in stringword:
            self.misteryword.append(char)

        # create pattern with only underscores with length of misteryword
        self.emptypattern = list("_" * len(self.misteryword))
        self.guessed = []

    def guess(self, letter):
        # Update the game for a guess of letter. Return True if the letter
        # is added to the pattern, return False if it is not.

        # assertion tests
        assertletter = str(letter)
        assert assertletter.isalpha()
        assert len(assertletter) == 1
        assert assertletter not in self.guessed

        # if guess is not letter, not single char or already guessed, return false
        if letter == None or len(letter) != 1 or (letter in self.emptypattern):
            return False
        else:

            # add guess to list with guessed letters
            self.guessed.append(letter)

            # subtract 1 from guesses left
            self.num_guesses -= 1

            # change underscore to letter if guessed letter is in misteryword
            if letter in self.misteryword:
                i = 0
                for c in self.misteryword:
                    if c == letter:
                        self.emptypattern[i] = c
                    i += 1

                return True

            # return false if guessed letter is not in mistery word
            return False

    def pattern(self):
        # Return a nice version of the pattern, for printing.
        self.stringword = "".join(map(str, self.emptypattern))
        return self.stringword

    def __str__(self):
        return self.pattern()

    def won(self):
        # Return True if the game is finished and the player has won,
        # otherwise False.

        # check if every character of the word is in guessed letters
        for char in range(self.length):
            # if char is not in misteryword, game not won --> return false
            if self.misteryword[char] not in self.guessed:
                return False

        # return True if game is finished and every letter is guessed
        return True

    def lost(self):
        # Return True if the game is finished and the player has lost,
        # otherwise False.
        if self.finished() == True and self.won() == False:
            # return True if game is finished and not won
            return True
        return False

    def finished(self):
        # Return True if the game is finished, otherwise False.

        # if guesses are gone, game finished --> return True
        if self.num_guesses == 0:
            return True

        # if pattern is guessed, game finished --> return True
        elif self.won() == True:
            return True
        else:
            return False

    def guessed_string(self):
        # Produce a string of all letters guessed so far, in the order they
        # were guessed.
        self.stringguess = " ".join(map(str, self.guessed))
        return self.stringguess


if __name__ == '__main__':
    while True:
        # Prompt the user for how many letters the Hangman word should have
        length = 0
        while True:
            length = int(input("How long do you want the word to be? "))
            if length > 1 and length < 28:
                break

        # Prompt the user for how many guesses she should get until she loses.
        num_guesses = 0
        while num_guesses <= 0:
            num_guesses = int(input("How many guesses do you want? "))

        # create hangman game
        game = Hangman(length, num_guesses)
        while game.finished() == False:

            # prompt user for guess
            while True:
                letter = input("Guess a letter: ")
                if letter in game.guessed:
                    print("You already guessed that letter, try again")
                else:
                    break

            # check guessed letter
            game.guess(letter)

            # print current state of game (pattern, guesses remaining etc)
            print(game.guessed)
            print(game.pattern())
            print(game.num_guesses)

        # if game is finished show response
        if game.won() == True:
            print("Congratulations, you won!")
        else:
            print(game.misteryword)

        # ask user if he/she wants to play again
        again = input("Do you want to play again? y/n")
        if again == 'n' or again == 'N':
            break