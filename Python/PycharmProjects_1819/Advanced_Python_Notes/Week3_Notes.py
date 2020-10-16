# Playing Cards
import random

SUIT_NAMES = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANK_NAMES = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9',
              '10', 'Jack', 'Queen', 'King']


class Card:
    """A single playing card.

    Attributes:
        suit: integer 0-3
        rank: integer 1-13
    """

    def __init__(self, rank, suit):
        """Initialize the card.

        :param rank: an integer 1-13 representing the rank
        :param suit: an integer 0-3 representing the suit
        """
        if rank < 1 or rank > 13:
            raise ValueError("[ rank must be in range 1-13 ]")
        if suit < 0 or suit > 3:
            raise ValueError("[ suit must be in range 0-3 ]")
        self.rank = rank
        self.suit = suit

    def to_string(self):
        """Return a human readable string representation of the card."""
        return f'{RANK_NAMES[self.rank]} of {SUIT_NAMES[self.suit]}'


class Deck:
    """A deck of playing cards.

    Attributes:
        cards: list of playing cards
    """

    def __init__(self):
        """Initialize a deck of playing cards.

        Deck is not shuffled on initialization.
        """
        self.cards = []
        for suit in range(len(SUIT_NAMES)):
            for rank in range(1, len(RANK_NAMES)):
                card_to_add = Card(rank, suit)
                self.cards.append(card_to_add)

    def is_empty(self):
        """Return if the deck is empty or not.

        :return Boolean
        """
        if len(self.cards) == 0:
            return True
        else:
            return False

    def draw_card(self):
        """Remove and return the top of the deck.

        :return Card
        """
        return self.cards.pop()

    def shuffle(self):
        """Shuffle the cards in the deck."""
        random.shuffle(self.cards)


class Hand:
    """A player's hand.

    Attributes:
        cards: list of cards in the hand
    """

    def __init__(self):
        """Initialize hand to be empty."""
        self.cards = []

    def draw_card(self):
        """Remove and return the top of the hand.

        :return Card
        """
        return self.cards.pop()

    def shuffle(self):
        """Shuffle the cards in the hand."""
        random.shuffle(self.cards)

    def add_card(self, card):
        """Add a card to the top of the hand.

        :param card: Card to add
        """
        self.cards.append(card)

    def is_empty(self):
        """Return if the hand is empty or not.

        :return Boolean
        """
        if len(self.cards) == 0:
            return True
        else:
            return False


def main():
    deck = Deck()
    for card in deck.cards:
        print(card.to_string())


if __name__ == "__main__":
    main()

