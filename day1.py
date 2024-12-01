# day 1 of advent of code 2024

def read_input():
    """Read input columns from stdin."""
    first_column, second_column = [], []
    while True:
        try:
            line = input()
            first, second = map(int, line.split())
            first_column.append(first)
            second_column.append(second)
        except (ValueError, EOFError):
            break
    return first_column, second_column

def calculate_min_distance(first_col, second_col):
    """Calculate minimum distance between sorted lists."""
    sorted_first = sorted(first_col)
    sorted_second = sorted(second_col)
    return sum(abs(a - b) for a, b in zip(sorted_first, sorted_second))

def calculate_similarity(first_col, second_col):
    """Calculate similarity score by counting occurrences."""
    second_counts = {}
    for num in second_col:
        second_counts[num] = second_counts.get(num, 0) + 1
    
    return sum(num * second_counts.get(num, 0) for num in first_col)

def main():
    first_col, second_col = read_input()
    print(calculate_min_distance(first_col, second_col))
    print("Similarity")
    print(calculate_similarity(first_col, second_col))

if __name__ == "__main__":
    main()