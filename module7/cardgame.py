# Implements a cards shuffler and dealer.
import random

# class Card 'reads' the card and prints what type of card it is
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # prints type of card: "A of hearts"
    def description(self):
        return f"{self.value} of {self.suit}"

# class Deck creates a deck of hearts, shuffles and deals one card
class Deck:
    def __init__(self):
        self._suits = ['Hearts','Diamonds','Clubs','Spades']
        self._values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self._cards = []
        
        # fill list _cards with every possible card
        for s in self._suits:
            for v in self._values:
                self._cards.append(Card(s,v))

    # shuffle the deck    
    def shuffle(self):
        random.shuffle(self._cards)

    # deal the top card
    def deal(self):
        return self._cards.pop()

    # print the size of the deck of cards (list _cards)
    def description(self):
        return f"{len(self._cards)} cards in the deck"

if __name__ == "__main__":   

    # create new deck of cards
    deck = Deck()

    # shuffle deck
    deck.shuffle()

    # deal one card from deck
    card = deck.deal()

    # print the type of card
    print(card.description())

    # print size of deck
    print(deck.description())
