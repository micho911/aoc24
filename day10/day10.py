def make_map_grid(input_data):
    return [list(map(int, line.strip())) for line in input_data.splitlines()]

def find_trailheads(grid):
    trailheads = []
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == 0:
                trailheads.append((x, y))
    return trailheads

def find_trail(grid, start):
    from collections import deque

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left
    visited = set()
    queue = deque([(*start, 0)])  # (x, y, current_height)

    reachable_nines = set()
    while queue:
        x, y, height = queue.popleft()

        # Skip invalid or already visited positions
        if (x, y) in visited or not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
            continue

        # Skip positions that don't match the expected height
        if grid[y][x] != height:
            continue

        visited.add((x, y))

        # If we reached height 9, record it and stop further exploration
        if height == 9:
            reachable_nines.add((x, y))
            continue

        # Add neighboring positions to the queue
        for dx, dy in directions:
            queue.append((x + dx, y + dy, height + 1))

    return reachable_nines

def count_distinct_trails(grid, start):
    from functools import lru_cache

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left
    max_x, max_y = len(grid[0]), len(grid)

    @lru_cache(None)
    def dfs(x, y, current_height):
        # If out of bounds or wrong height, terminate this path
        if not (0 <= x < max_x and 0 <= y < max_y) or grid[y][x] != current_height:
            return 0

        # If we reached height 9, count this as a distinct trail
        if current_height == 9:
            return 1

        # Explore all valid directions for the next step
        next_height = current_height + 1
        count = 0
        for dx, dy in directions:
            count += dfs(x + dx, y + dy, next_height)

        return count

    return dfs(*start, 0)

def calculate_ratings(grid, trailheads):
    ratings = {}
    for trailhead in trailheads:
        ratings[trailhead] = count_distinct_trails(grid, trailhead)
    return ratings

def sum_ratings(ratings):
    return sum(ratings.values())

def calculate_scores(grid, trailheads):
    scores = {}
    for trailhead in trailheads:
        reachable_nines = find_trail(grid, trailhead)
        scores[trailhead] = len(reachable_nines)
    return scores

def sum_scores(scores):
    return sum(scores.values())

def read_input(filename):
    with open(filename, 'r') as f:
        return f.read()

def main():
    input_data = read_input('./day10/test.txt')
    grid = make_map_grid(input_data)

    trailheads = find_trailheads(grid)
    scores = calculate_scores(grid, trailheads)

    print(f"Trailhead Scores: {scores}")
    print(f"Total Score: {sum_scores(scores)}")

    day10 = read_input('./day10/day10.txt')
    grid = make_map_grid(day10)
    
    trailheads = find_trailheads(grid)
    scores = calculate_scores(grid, trailheads)

    print(f"Trailhead Scores: {scores}")
    print(f"Total Score: {sum_scores(scores)}")

    day10 = read_input('./day10/day10.txt')
    grid = make_map_grid(day10)

    trailheads = find_trailheads(grid)
    ratings = calculate_ratings(grid, trailheads)

    print(f"Trailhead Ratings: {ratings}")
    print(f"Sum of Trailhead Ratings: {sum_ratings(ratings)}")


if __name__ == "__main__":
    main()