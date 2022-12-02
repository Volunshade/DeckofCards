"""This module is for the suit of cards."""
from typing import Iterator


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


class Spade(Suit):
    """Representation of a spade."""

    def __init__(self):
        """Create a new instance."""

        name = "spade"
        symbol = u"\u2660"
        super().__init__(name, symbol)


class Heart(Suit):
    """Representation of a heart."""

    def __init__(self):
        """Create a new instance."""

        name = "heart"
        symbol = u"\u2665"
        super().__init__(name, symbol)


class Club(Suit):
    """Representation of a club."""

    def __init__(self):
        """Create a new instance."""

        name = "club"
        symbol = u"\u2663"
        super().__init__(name, symbol)


class Diamond(Suit):
    """Representation of a diamond."""

    def __init__(self):
        """Create a new instance."""

        name = "diamond"
        symbol = u"\u2666"
        super().__init__(name, symbol)


class Suits:
    """Representation of a suits manager."""

    def __init__(self) -> None:
        """Create a new instance."""

        self.suits = [Diamond(), Heart(), Club(), Spade()]

    def __len__(self) -> int:
        """Representation of the length."""

        return len(self.suits)

    def __iter__(self) -> Iterator[Suit]:
        """Representation of an iterable."""

        for suit in self.suits:
            yield suit

