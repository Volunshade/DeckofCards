"""This module is for a deck of cards."""
import random


class Suit:
    """Representation of a cards suit."""

    def __init__(self, name: str, symbol: str) -> None:
        """Create a new instance."""

        self.name = name
        self.symbol = symbol

    def __str__(self) -> str:
        """String representation of a suit."""

        return f"Suit(name={self.name}, symbol={self.symbol})"

    @property
    def color(self) -> str:
        """Determine the color of a suit."""

        color = None

        if self.name in ["heart", "diamond"]:
            color = "red"
        elif self.name in ["club", "spade"]:
            color = "black"
        else:
            raise Exception("Invalid suit name.")

        return color


class Card:
    """Representation of a card."""

    def __init__(self, name: str, value: int, suit: Suit) -> None:
        """Create a new instance."""

        self.name = name
        self.value = value
        self.suit = suit

    def __str__(self) -> str:
        """String representation of a card."""

        return f"Card(name={self.name}, value={self.value}, suit={self.suit})"


class Deck:
    """Representation of a deck."""

    def __init__(self):
        """Create a new instance."""

        self.cards = []

        suits = [
            ("heart", u"\u2665"),
            ("spade", u"\u2660"),
            ("club", u"\u2663"),
            ("diamond", u"\u2666")
        ]
        for _suit in suits:
            suit = Suit(*_suit)
            cards = [
                ("ace", 1, suit),
                ("two", 2, suit),
                ("three", 3, suit),
                ("four", 4, suit),
                ("five", 5, suit),
                ("six", 6, suit),
                ("seven", 7, suit),
                ("eight", 8, suit),
                ("nine", 9, suit),
                ("ten", 10, suit),
                ("jack", 10, suit),
                ("queen", 10, suit),
                ("king", 10, suit)
            ]
            for _card in cards:
                card = Card(*_card)
                self.cards.append(card)
    def shuffle(self):
        """Shuffles the deck of cards."""

        random.shuffle(self.cards)

    def deal_card(self):
        """Deal a card from the deck."""

        return self.cards.pop()


def main():
    """This will shuffle and deal a card from the deck."""

    deck = Deck()
    deck.shuffle()
    player_card = deck.deal_card()
    print(player_card)

    for card in deck.cards:
        print(card)

if __name__ == "__main__":
    main()
