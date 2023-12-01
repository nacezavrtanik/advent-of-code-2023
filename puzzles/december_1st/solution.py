"""Advent of Code 2023: 1st of December."""

from timer import timer


def insert_digits_between_words(document):
    """Insert digits between corresponding words.

    Note that the words are not simply replaced by digits. Words may overlap,
    so replacing them would not yield the correct answer due to improper
    substitution.
    """
    words = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    replacements = [(word, f"{word}{digit}{word}") for word, digit in zip(words, range(1, 10))]
    for replacement in replacements:
        document = document.replace(*replacement)
    return document


def sum_calibration_values(document):
    """Sum the concatenation of first and last digit of each line."""
    digits = {str(i) for i in range(1, 10)}
    first = previous = None
    result = 0
    for character in document:
        if character in digits:
            if not first:
                first = character
            previous = character
        if character == "\n":
            result += int(first + previous)
            first = None
    return result


@timer
def part_one():
    """Print solution to Part 1."""
    with open("puzzle_input.txt", "r") as document:
        print(sum_calibration_values(document.read()))


@timer
def part_two():
    """Print solution to Part 2."""
    with open("puzzle_input.txt", "r") as document:
        print(sum_calibration_values(insert_digits_between_words(document.read())))


def main():
    """Solve puzzles."""
    part_one()
    part_two()


if __name__ == "__main__":
    main()
