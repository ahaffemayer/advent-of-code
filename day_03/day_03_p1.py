import re
import numpy as np


def read_input(file_path: str) -> str:
    """
    Reads the input file and returns the content as a string.
    Assumes the corrupted memory is stored as a single line.
    """
    with open(file_path, "r") as file:
        return file.read().strip()


def extract_mul_instructions(memory: str) -> list:
    """
    Extracts valid 'mul(X,Y)' instructions from the corrupted memory string.
    Returns a list of (X, Y) integer tuples.
    """
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, memory)
    return [(int(x), int(y)) for x, y in matches]


def calculate_products(pairs: list) -> np.ndarray:
    """
    Calculates the product of each (X, Y) pair.
    Returns a NumPy array of the results.
    """
    return np.array([x * y for x, y in pairs])


def sum_products(products: np.ndarray) -> int:
    """
    Returns the sum of the products.
    """
    return np.sum(products)


if __name__ == "__main__":
    # Step 1: Read corrupted memory string
    memory_string = read_input("input.txt")

    # Step 2: Extract valid mul(X,Y) instructions
    pairs = extract_mul_instructions(memory_string)

    # Step 3: Calculate all products
    products = calculate_products(pairs)

    # Step 4: Sum the results
    total = sum_products(products)

    print(f"The sum of all valid mul(X,Y) results is: {total}")
