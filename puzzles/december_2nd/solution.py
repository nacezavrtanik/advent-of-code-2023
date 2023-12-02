"""Advent of Code 2023: 2nd of December."""

from enum import StrEnum, auto
from collections import namedtuple
from functools import reduce

from timer import timer


class Color(StrEnum):
    """Color constant strings."""
    RED = auto()
    GREEN = auto()
    BLUE = auto()


class Cubes(namedtuple("Cubes", Color)):
    """A set of red, green, and blue cubes."""
    __slots__ = ()

    @property
    def total(self):
        """Return the total number of cubes."""
        return sum(self)

    @property
    def power(self):
        """Return the product of the number of cubes of each color."""
        return reduce(lambda x, y: x*y, self)

    @classmethod
    def from_string(cls, input_string):
        """Construct a Cubes object from a specific string."""
        kwargs = {}
        for color in Color:
            kwargs[color] = 0
            for entry in input_string.split(","):
                if entry.endswith(color):
                    kwargs[color] = int(entry.replace(color, ""))
                    break
        return cls(**kwargs)

    def __le__(self, other):
        """Compare all members rather than just the first."""
        return all([self_ <= other_ for self_, other_ in zip(self, other)])


class Game:
    """A game with its number and its corresponding sets of seen cubes."""
    def __init__(self, number, cubes_list):
        """Initiate the object."""
        self.number = number
        self.cubes_list = cubes_list

    @classmethod
    def from_string(cls, input_string):
        """Construct a Game object from a line of the puzzle input."""
        input_string = input_string.replace(" ", "").replace("\n", "").replace("Game", "")
        number_string, cubes_list_string = input_string.split(":")
        number = int(number_string)
        cubes_list = [Cubes.from_string(cubes_string) for cubes_string in cubes_list_string.split(";")]
        return cls(number, cubes_list)

    def is_possible(self, available_cubes):
        """Return True if the game is possible for a given set of cubes."""
        return all([cubes <= available_cubes and cubes.total <= available_cubes.total for cubes in self.cubes_list])

    def minimum_cubes(self):
        """Return the cubes object with the minimal number for each color."""
        return Cubes(*[max(color) for color in zip(*self.cubes_list)])


@timer
def part_one():
    """Print solution to Part 1."""
    available_cubes = Cubes(red=12, green=13, blue=14)
    with open("puzzle_input.txt", "r") as games_info:
        result = 0
        for line in games_info:
            game = Game.from_string(line)
            if game.is_possible(available_cubes):
                result += game.number
    print(result)


@timer
def part_two():
    """Print solution to Part 2."""
    with open("puzzle_input.txt", "r") as game_info:
        result = sum([Game.from_string(line).minimum_cubes().power for line in game_info])
    print(result)


def main():
    """Solve puzzles."""
    part_one()  # part_one executed in: 0.0020 seconds
    part_two()  # part_two executed in: 0.0017 seconds


if __name__ == "__main__":
    main()
