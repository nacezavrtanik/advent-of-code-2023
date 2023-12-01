"""Advent of Code 2023: Module for the `timer` decorator."""

import time


def timer(function):
    """Measure execution time of decorated function."""
    def wrapper(*args, **kwargs):
        start = time.time()
        output = function(*args, **kwargs)
        end = time.time()
        print(f"{function.__name__} executed in: {end-start:.4f} seconds\n")
        return output
    return wrapper
