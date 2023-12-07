
from enum import IntEnum, auto
from collections import Counter


class HandType(IntEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    FIVE_OF_A_KIND = auto()


Card = IntEnum("Card", [str(i) for i in range(2, 10)] + ["T", "J", "Q", "K", "A"])


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    @property
    def type_(self):
        count_of_same_cards = sorted(list(Counter(self.cards).values()), reverse=True)
        match count_of_same_cards:
            case [1, 1, 1, 1, 1]:
                return HandType.HIGH_CARD
            case [2, 1, 1, 1]:
                return HandType.ONE_PAIR
            case [2, 2, 1]:
                return HandType.TWO_PAIR
            case [3, 1, 1]:
                return HandType.THREE_OF_A_KIND
            case [3, 2]:
                return HandType.FULL_HOUSE
            case [4, 1]:
                return HandType.FOUR_OF_A_KIND
            case [5]:
                return HandType.FIVE_OF_A_KIND

    @classmethod
    def from_string(cls, input_string):
        hand, bid_string = input_string.replace("\n", "").split(" ")
        bid = int(bid_string)
        return cls(hand, bid)

    def __lt__(self, other):
        if self.type_ != other.type_:
            return self.type_ < other.type_

        for self_card, other_card in zip(self.cards, other.cards):
            self_card = getattr(Card, self_card)
            other_card = getattr(Card, other_card)
            if self_card != other_card:
                return self_card < other_card

        return False


with open("puzzle_input.txt", "r") as puzzle_input:
    hands = sorted([Hand.from_string(line) for line in puzzle_input])

result = sum([hand.bid * (hands.index(hand)+1) for hand in hands])
