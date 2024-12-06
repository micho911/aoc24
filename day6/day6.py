import copy
from datetime import datetime

def get_direction(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char in '^v<>':
                return char, (x, y)
    return None, (0, 0)

def make_map(lines):
    return [list(line) for line in lines.splitlines()]

def read_input(filename):
    with open(filename, 'r') as file:
        return file.read()

def simulate(grid, detect_loop=False):
    dir_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction_symbols = {'^': 0, '>': 1, 'v': 2, '<': 3}

    start_dir_symbol, (x, y) = get_direction(grid)
    if start_dir_symbol is None:
        raise ValueError("No guard found on the map.")

    current_dir_index = direction_symbols[start_dir_symbol]
    grid[y][x] = 'X'

    rows, cols = len(grid), len(grid[0])
    visited_states = set([(x, y, current_dir_index)])

    while True:
        dx, dy = dir_list[current_dir_index]
        nx, ny = x + dx, y + dy

        if ny < 0 or ny >= rows or nx < 0 or nx >= cols:
            return grid if not detect_loop else False

        if grid[ny][nx] == '#':
            current_dir_index = (current_dir_index + 1) % 4
            continue
        
        x, y = nx, ny
        grid[y][x] = 'X'

        state = (x, y, current_dir_index)
        if detect_loop and state in visited_states:
            return True
        
        visited_states.add(state)

def count_x(grid):
    return sum(line.count('X') for line in grid)

def would_loop(original_grid, obstruction_pos):
    temp_grid = copy.deepcopy(original_grid)
    ox, oy = obstruction_pos

    if temp_grid[oy][ox] != '.':
        return False

    temp_grid[oy][ox] = '#'

    try:
        return simulate(temp_grid, detect_loop=True)
    except ValueError:
        return False

def find_loop_obstructions(grid):
    loop_obstructions = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] not in ['#', '^', 'v', '<', '>']:
                if would_loop(grid, (x, y)):
                    loop_obstructions.append((x, y))
    return loop_obstructions

def main():
    real_input = read_input('./day6/day6.txt')
    real_map = make_map(real_input)

    print("Part 1 - Test cases")
    test_input = read_input('./day6/test.txt')  
    assert count_x(simulate(make_map(test_input))) == 41
    print("All test cases passed")

    # Part 1: Simulate and count 'X'
    startTime = datetime.now()
    simulated_map = simulate(copy.deepcopy(real_map))
    print("Part 1 - Execution time:", datetime.now() - startTime)
    print("Part 1 - Cells visited:", count_x(simulated_map))

    print("Part 2 - Test cases")
    len(find_loop_obstructions(make_map(test_input))) == 6
    print("All test cases passed")
    # Part 2: Find loop obstructions
    startTime = datetime.now()
    loop_positions = find_loop_obstructions(real_map)
    print("Part 2 - Execution time:", datetime.now() - startTime)
    print("Part 2 - Obstruction count:", len(loop_positions))

if __name__ == "__main__":
    main()