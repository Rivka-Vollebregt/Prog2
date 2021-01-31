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

        # load the dictionary of words
        file = open('dictionary.txt', 'r')

        # put words in list
        for line in file:
            line = line.strip()
            self.words.append(line)

    # return a list of all words from the dictionary of the given length
    def get_words(self, length):

        # create new list
        self.correctlength_list = []

        # add words of correct length in correctlength_list
        for word in self.words:
            if len(word) == length:
                self.correctlength_list.append(word)
        return self.correctlength_list

    # return a single random word of given length. Uses `get_words` above
    def get_word(self, length):
        return random.choice(self.get_words(length))


class Hangman:

    # initialize game by choosing a word and creating an empty pattern
    def __init__(self, length, num_guesses):
        self.length = length
        self.num_guesses = num_guesses

        # assertions for length of word and guesses
        assert length > 1 and length < 29
        assert length != 26
        assert num_guesses > 1 and num_guesses < 27

        lex = Lexicon()
        randomword = lex.get_word(length)
        self.misteryword = []

        # store chosen word in misteryword
        for char in randomword:
            self.misteryword.append(char)

        # create pattern with only underscores with length of misteryword
        self.emptypattern = list("_" * len(self.misteryword))
        self.guessed = []

    # update the game for a guess of letter: return True if letter in pattern, else False
    def guess(self, letter):

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

            # change underscore to letter if guessed letter is in misteryword
            if letter in self.misteryword:
                position = 0
                for char in self.misteryword:
                    if char == letter:
                        self.emptypattern[position] = char
                    position += 1
                return True

            # subtract 1 from guesses left if guess was wrong
            self.num_guesses -= 1

            # return false if guessed letter is not in mistery word
            return False

    # return a nice version of the pattern, for printing
    def pattern(self):
        return "".join(map(str, self.emptypattern))

    # return True if the game is finished and player won, else False
    def won(self):

        # check if every character of the word is in guessed letters
        for char in range(self.length):
            # if char is not in misteryword, game not won --> return false
            if self.misteryword[char] not in self.guessed:
                return False

        # return True if game is finished and every letter is guessed
        return True

    # return True if the game is finished and player lost, else False
    def lost(self):
        if self.finished() == True and self.won() == False:
            return True
        return False

    # return True if the game is finished, otherwise False
    def finished(self):

        # if guesses are gone, game finished --> return True
        if self.num_guesses == 0:
            return True

        # if pattern is guessed, game finished --> return True
        elif self.won() == True:
            return True
        else:
            return False

    # return string of letters guessed so far, in the order they were guessed
    def guessed_string(self):
        return " ".join(map(str, self.guessed))


if __name__ == '__main__':
    while True:

        # prompt the user for how many letters the Hangman word should have
        length = 0
        while True:
            length = int(input("How long do you want the word to be? "))
            if length > 1 and length < 28:
                break

        # prompt the user for how many guesses she should get until she loses
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

            # print current state of game (guessed letters,pattern, guesses remaining)
            print(game.guessed)
            print(game.pattern())
            print(game.num_guesses)

        # if game is finished show response
        if game.won() == True:
            print("Congratulations, you won!")
        else:
            print(game.misteryword)
            print("You lost, better luck next time!")

        # ask user if he/she wants to play again
        again = input("Do you want to play again? y/n")
        if again == 'n' or again == 'N':
            break