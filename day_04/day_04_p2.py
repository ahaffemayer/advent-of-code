import os
os.chdir(os.path.dirname(__file__))


def read_grid(file_path: str) -> list:
    """
    Reads the grid from a file and returns it as a list of list of characters.
    """
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file if line.strip()]


def is_mas_triplet(a: str, b: str, c: str) -> bool:
    """
    Checks if the three characters form MAS or SAM.
    """
    return [a, b, c] == ['M', 'A', 'S'] or [a, b, c] == ['S', 'A', 'M']


def count_x_mas_patterns(grid: list) -> int:
    """
    Counts the number of X-MAS patterns in the grid.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            try:
                # Diagonal ↖ (r-1,c-1), (r,c), (r+1,c+1)
                d1 = [grid[r - 1][c - 1], grid[r][c], grid[r + 1][c + 1]]
                # Diagonal ↗ (r-1,c+1), (r,c), (r+1,c-1)
                d2 = [grid[r - 1][c + 1], grid[r][c], grid[r + 1][c - 1]]

                if is_mas_triplet(*d1) and is_mas_triplet(*d2):
                    count += 1
            except IndexError:
                continue

    return count


if __name__ == "__main__":
    grid = read_grid("input.txt")
    total = count_x_mas_patterns(grid)
    print(f"Total X-MAS patterns found: {total}")
