import os
os.chdir(os.path.dirname(__file__))


def read_grid(file_path: str) -> list:
    """
    Reads the grid from a file and returns it as a list of list of characters.
    """
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file if line.strip()]


def count_xmas_occurrences(grid: list) -> int:
    """
    Counts all occurrences of 'XMAS' in all 8 directions in the grid.
    """
    target = "XMAS"
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Define directions: (dx, dy)
    directions = [
        (0, 1),   # →
        (0, -1),  # ←
        (1, 0),   # ↓
        (-1, 0),  # ↑
        (1, 1),   # ↘
        (1, -1),  # ↙
        (-1, 1),  # ↗
        (-1, -1)  # ↖
    ]

    count = 0

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                match = True
                for i in range(4):
                    nr, nc = r + i * dr, c + i * dc
                    if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == target[i]):
                        match = False
                        break
                if match:
                    count += 1

    return count


if __name__ == "__main__":
    grid = read_grid("input.txt")
    total = count_xmas_occurrences(grid)
    print(f"Total occurrences of 'XMAS': {total}")
