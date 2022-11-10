"""This module is for a deck of cards."""
import random


class Suit:
    """Representation of a cards suit."""

    def __init__(self, name: str, symbol: str) -> None:
        """Create a new instance."""

        self.name = name
        self.symbol = symbol
        self.color = self.get_color()

    def get_color(self) -> str:
        """Determine the color of a suit."""

        color = None

        if self.name in ["heart", "diamond"]
            color = red
        elif self.name in ["club", "spade"]
            color = black
        else:
            raise Exception("Invalid suit name.")

        return color


class Card:
    """Representation of a card."""

    def __init__(self, value: str, name: str, suit: Suit):
        """Create a new instance."""

        self.value = value
        self.name = name
        self.suit = suit
  

class Deck:
    """Representation of a deck."""

    def __init__(self):
        """Create a new instance."""

        self.cardlist = []


        pass

    def shuffle_deck(self):
        """Shuffles the deck of cards."""

        self.shuffled_deck = random.shuffle()

        pass

    def deal_card(self):
        """Deal a card from the deck."""

        pass


def main():
    """This will shuffle and deal a card from the deck"""

    pass


if __name__ == "__main__"
    main()
