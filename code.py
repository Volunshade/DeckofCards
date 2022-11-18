"""This module is for a deck of cards."""
import random


class Suit:
    """Representation of a cards suit."""

    def __init__(self, name: str, symbol: str) -> None:
        """Create a new instance."""

        self.name = name
        self.symbol = symbol

    @property
    def color(self) -> str:
        """Determine the color of a suit."""

        color = None

        if self.name in ["heart", "diamond"]
            color = "red"
        elif self.name in ["club", "spade"]
            color = "black"
        else:
            raise Exception("Invalid suit name.")

        return color


class Card:
    """Representation of a card."""

    def __init__(self, name: str, value: str, suit: Suit):
        """Create a new instance."""

        self.name = name
        self.value = value
        self.suit = suit
  

class Deck:
    """Representation of a deck."""

    def __init__(self):
        """Create a new instance."""

        self.cardlist = []

        cards = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]
        suits = ["heart", "diamond", "spade", "club"]
        for card in self.cards:
            for suit in self.suits:
                self.cardlist.append(Card(value,suit))

    def shuffle(self):
        """Shuffles the deck of cards."""

        self.shuffled = random.shuffle()

    def deal_card(self):
        """Deal a card from the deck."""

        pass


def main():
    """This will shuffle and deal a card from the deck."""

    pass


if __name__ == "__main__"
    main()
