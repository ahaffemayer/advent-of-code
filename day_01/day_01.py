import numpy as np

def read_input(file_path: str) -> list:
    """
    Reads the input file and returns a list of integers.
    Each line in the file is expected to contain a single integer.
    """
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            # Strip whitespace and check if the line is not empty
            n1, n2 = line.strip().split("   ")
            if n1 and n2:
                # Convert the line to a list of integers
                data.append([int(n1), int(n2)])
    return data

def sort_data(data: list) -> list:
    """
    Sorts the data based on the first element of each sublist.
    """
    l1 = [x[0] for x in data]
    l2 = [x[1] for x in data]
    
    l1_sorted = np.sort(l1)
    l2_sorted = np.sort(l2)
    return list(zip(l1_sorted, l2_sorted))

def calculate_differences(data: list) -> list:
    """
    Calculates the differences between the first and second elements of each sublist.
    """
    return [abs(n1 - n2) for n1, n2 in data]

def calculate_sum(difference_data: list) -> int:
    """
    Calculates the sum of the differences.
    """
    return sum(difference_data)

if __name__ == "__main__":
    # Read the input file
    data = read_input('input.txt')
    # Sort the data
    data = sort_data(data)
    # Calculate the differences
    differences = calculate_differences(data)
    # Calculate the sum of the differences
    total_sum = calculate_sum(differences)
    print(f"The sum of the differences is: {total_sum}")
    