def find_xmas_occurrences(grid):
    unique_occurrences = set()

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
    ]

    def check_word(x, y, dx, dy, reverse=False):
        word = ['X', 'M', 'A', 'S'] if not reverse else ['S', 'A', 'M', 'X']
        
        if (0 <= x + 3*dx < len(grid) and 
            0 <= y + 3*dy < len(grid[0])):
            if all(grid[x + i*dx][y + i*dy] == word[i] for i in range(4)):
                start = (x, y)
                end = (x + 3*dx, y + 3*dy)
                return tuple(sorted([start, end]))
        return None

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                result = check_word(x, y, dx, dy)
                if result:
                    unique_occurrences.add(result)
                result_reverse = check_word(x, y, dx, dy, reverse=True)
                if result_reverse:
                    unique_occurrences.add(result_reverse)

    return len(unique_occurrences)

def find_x_mas_occurrences(grid):
    unique_centers = set()
    rows = len(grid)
    cols = len(grid[0])

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if grid[x][y] != 'A':
                continue 
            c1 = grid[x - 1][y - 1]
            c2 = grid[x - 1][y + 1]
            c3 = grid[x + 1][y - 1]
            c4 = grid[x + 1][y + 1]

            diagonal1_chars = {c1, c4}
            valid_diagonal1 = diagonal1_chars == {'M', 'S'}

            diagonal2_chars = {c2, c3}
            valid_diagonal2 = diagonal2_chars == {'M', 'S'}

            if valid_diagonal1 and valid_diagonal2:
                unique_centers.add((x, y))

    return len(unique_centers)

def read_grid(filename):
    with open(filename, "r") as file:
        return [list(line.strip()) for line in file]

if __name__ == "__main__":
    grid = read_grid("input.txt")
    xmas_count = find_xmas_occurrences(grid)
    print(f"\nTotal unique XMAS occurrences: {xmas_count}")
    x_mas_count = find_x_mas_occurrences(grid)
    print(f"\nTotal unique X-MAS occurrences: {x_mas_count}")