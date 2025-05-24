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
            n1, n2 = line.strip().split("   ")
            if n1 and n2:
                # Convert the line to a list of integers
                data.append([int(n1), int(n2)])
    return data

def compute_similarity(data: list) -> list:
    """
    Computes the similarity between the first and second elements of each sublist.
    """
    sim = 0
    l1 = [x[0] for x in data]
    l2 = [x[1] for x in data]
    
    for n in l1:
        sim += l2.count(n) * n 
    return sim
        
    

if __name__ == "__main__":
    # Read the input file
    data = read_input("input.txt")
    # Compute the similarity
    similarity = compute_similarity(data)
    print(f"The similarity is: {similarity}")