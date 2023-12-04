"""Advent of Code 2023: 4th of December."""

from timer import timer


class Card:
    """A scratchcard with its id number, winning number, and having numbers."""
    def __init__(self, number, winning, having):
        """Initiate the object."""
        self.number = number
        self.winning = winning
        self.having = having

    @property
    def winning_among_having(self):
        """Return the set of having numbers which are winning numbers."""
        return self.having.intersection(self.winning)

    @property
    def points(self):
        """Return the number of points the card is worth."""
        return 2 ** (len(self.winning_among_having)-1) if self.winning_among_having else 0

    @classmethod
    def from_string(cls, input_string):
        """Construct a Came object from a line of the puzzle input."""
        input_string = input_string.replace("Card", "").replace("\n", "")
        number_string, winning_having_string = input_string.split(":")
        number = int(number_string.strip())
        winning, having = [{int(i.strip()) for i in s.split(" ") if i.strip()}
                           for s in winning_having_string.split("|")]
        return cls(number, winning, having)


@timer
def part_one():
    """Print solution to Part 1."""
    with open("puzzle_input.txt", "r") as card_strings:
        result = sum([Card.from_string(card_string).points for card_string in card_strings])
        print(result)


@timer
def part_two():
    """Print solution to Part 2."""
    with open("puzzle_input.txt", "r") as card_strings:
        total_cards = {}
        original_card_only = 1
        for i, card_string in enumerate(card_strings):
            card = Card.from_string(card_string)
            if i not in total_cards:
                total_cards[i] = original_card_only
            for j in range(len(card.winning_among_having)):
                k = i + j + 1
                if k not in total_cards:
                    total_cards[k] = original_card_only
                total_cards[k] += total_cards[i]
    result = sum(total_cards.values())
    print(result)


def main():
    """Solve puzzles."""
    part_one()  # part_one executed in: 0.0017 seconds
    part_two()  # part_two executed in: 0.0019 seconds


if __name__ == "__main__":
    main()
