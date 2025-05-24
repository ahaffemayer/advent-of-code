import numpy as np


def read_input(file_path: str) -> list:
    """
    Reads the input file and returns a list of integers.
    Each line in the file is expected to contain a single integer.
    """
    data = []
    with open(file_path, "r") as file:
        for line in file:
            # Strip whitespace and check if the line is not empty
            data.append(line.strip().split(" "))
    return data


def from_char_to_int(line: list) -> list:
    """
    Convert the line from characters to integers.
    """
    return [int(x) for x in line]


def is_safe(line: list) -> bool:
    """
    Check if the line is safe.
    """
    diffs = [line[i + 1] - line[i] for i in range(len(line) - 1)]

    # Check if all differences are positive (increasing) or negative (decreasing)
    all_increasing = all(d > 0 for d in diffs)
    all_decreasing = all(d < 0 for d in diffs)

    # Check if all differences are in allowed range
    all_valid_diffs = all(1 <= abs(d) <= 3 for d in diffs)

    return (all_increasing or all_decreasing) and all_valid_diffs


def is_safe_with_dampener(line: list) -> bool:
    """
    Return True if the line is safe or can be made safe by removing one element.
    """
    if is_safe(line):
        return True
    for i in range(len(line)):
        shortened = line[:i] + line[i + 1 :]
        if is_safe(shortened):
            return True
    return False


if __name__ == "__main__":
    # Read the input file
    data = read_input("input.txt")
    data = [from_char_to_int(line) for line in data]
    # Count how many lines are safe
    safe_with_dampener_count = sum(is_safe_with_dampener(line) for line in data)
    print(f"Number of safe reports with dampener: {safe_with_dampener_count}")
