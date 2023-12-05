"""Advent of Code 2023: 5th of December."""

import time
from itertools import count

from timer import timer


def extract_seeds_and_maps(input_string):
    """Parse puzzle input."""
    seeds_string, *map_strings = input_string.split("\n\n")
    seeds = [int(seed_string) for seed_string in seeds_string.replace("seeds: ", "").split(" ")]
    maps = [map_string.split(":\n")[1] for map_string in map_strings]
    maps = [m.split("\n") for m in maps]
    maps = [[x.split(" ") for x in y] for y in maps]
    return seeds, maps


def _map_seed_once(seed, map_, inverse=False):
    """Apply a single map on a seed."""
    for line in map_:
        destination, source, range_ = map(int, line)
        if inverse:
            source, destination = destination, source
        if source <= seed < source+range_:
            seed_index = seed - source
            seed = destination + seed_index
            break
    return seed


def map_seed_to_location(seed, maps, inverse=False):
    """Apply consecutive maps to get location from seed."""
    for map_ in maps[::-1] if inverse else maps:
        seed = _map_seed_once(seed, map_, inverse=inverse)
    return seed


def _seed_is_valid(seed, seeds):
    """Return True if seed is in one of the valid ranges, False otherwise."""
    for start, range_ in [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]:
        if start <= seed < start+range_:
            return True
    return False


def find_valid_location(seeds, maps, start, step, until):
    """Check location candidates and return valid location if found.

    Candidates are chosen by starting at `start` and moving by `step`
    (may be negative). Parameter `until` must be either "first" or "last".
    If "first", the first encountered valid location is returned. If "last",
    the last valid location before again encountering an invalid location
    is returned.
    """
    if until not in {"first", "last"}:
        raise ValueError(f"Argument 'until' not equal to 'first' or 'last': {until}")
    start_time = time.time()

    location_candidates = count(start, step)
    last_valid_location = None

    while True:
        candidate = next(location_candidates)
        seed = map_seed_to_location(candidate, maps, inverse=True)

        if _seed_is_valid(seed, seeds):
            last_valid_location = candidate
            if until == "first":
                return last_valid_location
        else:
            if until == "last" and last_valid_location:
                return last_valid_location

        time_elapsed = time.time() - start_time
        if time_elapsed > 60:
            raise TimeoutError("Execution time exceeded 60 seconds")


@timer
def part_one():
    """Print solution to Part 1."""
    with open("puzzle_input.txt", "r") as almanac:
        seeds, maps = extract_seeds_and_maps(almanac.read())
    result = min([map_seed_to_location(seed, maps) for seed in seeds])
    print(result)


@timer
def part_two():
    """Print solution to Part 2.

    This function is not guaranteed to find the lowest valid location,
    however, it succeeds in doing so on the given puzzle input data. For
    different data, tweaking the parameters of the calls to
    `find_valid_location` should provide the desired results. (Note that
    by setting both start=0 and step=1, one is guaranteed to find the lowest
    valid location, should the function finish executing before the impending
    heat death of the universe.)

    This solution is loosely based on the observation that, due to the nature
    of the maps, valid locations come in batches, i.e. if a number `n` is a
    valid location, likely, so are `n-1` and `n+1`.
    """
    with open("puzzle_input.txt", "r") as almanac:
        seeds, maps = extract_seeds_and_maps(almanac.read())
    location_1 = find_valid_location(seeds, maps, 0, 10000, "first")  # find a batch of valid locations
    location_2 = find_valid_location(seeds, maps, location_1, -1, "last")  # find the smallest location in the batch
    print(location_2)


def main():
    """Solve puzzles."""
    part_one()  # part_one executed in: 0.0011 seconds
    part_two()  # part_two executed in: 0.3449 seconds


if __name__ == "__main__":
    main()
