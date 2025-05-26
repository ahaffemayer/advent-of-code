import re
import numpy as np


def read_input(file_path: str) -> str:
    """
    Reads the input file and returns the content as a string.
    Assumes the corrupted memory is stored as a single line.
    """
    with open(file_path, "r") as file:
        return file.read().strip()


def process_instructions(memory: str) -> int:
    """
    Processes the memory string, handling do(), don't(), and valid mul(X,Y) instructions.
    Returns the sum of the results of enabled multiplications.
    """
    # Pattern to match either do(), don't(), or valid mul(X,Y)
    pattern = r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.finditer(pattern, memory)

    mul_enabled = True
    results = []

    for match in matches:
        if match.group(0) == "do()":
            mul_enabled = True
        elif match.group(0) == "don't()":
            mul_enabled = False
        else:
            # It's a mul(X,Y) match
            x, y = int(match.group(1)), int(match.group(2))
            if mul_enabled:
                results.append(x * y)

    return np.sum(results)


if __name__ == "__main__":
    memory_string = read_input("input.txt")
    total = process_instructions(memory_string)
    print(f"The sum of enabled mul(X,Y) results is: {total}")
