
def get_antenna_locations(grid):
    antenna_locations = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char.isalnum():
                if char not in antenna_locations:
                    antenna_locations[char] = []
                antenna_locations[char].append((x, y))
    return antenna_locations

def find_antinode(antenna_locations, grid):
    antinode_locations = {}
    for char, locations in antenna_locations.items():
        for i, loc1 in enumerate(locations):
            for loc2 in locations[i+1:]:      
                dx = loc2[0] - loc1[0]
                dy = loc2[1] - loc1[1]
                antinode1 = loc1[0] - dx, loc1[1] - dy
                antinode2 = loc2[0] + dx, loc2[1] + dy
                if char not in antinode_locations:
                    antinode_locations[char] = set()
                if 0 <= antinode1[0] < len(grid[0]) and 0 <= antinode1[1] < len(grid):
                    antinode_locations[char].add(antinode1)
                if 0 <= antinode2[0] < len(grid[0]) and 0 <= antinode2[1] < len(grid):
                    antinode_locations[char].add(antinode2)
    return antinode_locations

def find_antinodes_with_resonant(antenna_locations, grid):
    ant_locs = {}
    for char, locations in antenna_locations.items():
        for i, loc1 in enumerate(locations):
            for loc2 in locations[i+1:]:      
                dx = loc2[0] - loc1[0]
                dy = loc2[1] - loc1[1]
                if char not in ant_locs:
                    ant_locs[char] = set()
                ant_locs[char].add(loc1)
                ant_locs[char].add(loc2)
                
                for i in range(len(grid)):
                    antinode1 = loc1[0] - dx * i, loc1[1] - dy * i
                    antinode2 = loc2[0] + dx * i, loc2[1] + dy * i
                    if char not in ant_locs:
                      ant_locs[char] = set()
                    if 0 <= antinode1[0] < len(grid[0]) and 0 <= antinode1[1] < len(grid):
                      ant_locs[char].add(antinode1)
                    if 0 <= antinode2[0] < len(grid[0]) and 0 <= antinode2[1] < len(grid):
                      ant_locs[char].add(antinode2)
    return ant_locs
  
def count_unique_antinode(antinode_locations):
    unique_antinode_locations = set()
    for locations in antinode_locations.values():
        for loc in locations:
            unique_antinode_locations.add(loc)
    return len(unique_antinode_locations)

def make_grid(input_data):
    grid = []
    for line in input_data.strip().splitlines():
        grid.append(list(line))
    return grid

read_input = lambda filename: open(filename, 'r').read()
def main():
    test = read_input('./day8/test.txt')
    grid = make_grid(test)

    assert count_unique_antinode(find_antinode(get_antenna_locations(grid), grid)) == 14

    assert count_unique_antinode(find_antinodes_with_resonant(get_antenna_locations(grid), grid)) == 34
    

    data = read_input('./day8/day8.txt')
    grid = make_grid(data)

    print(count_unique_antinode(find_antinodes_with_resonant(get_antenna_locations(grid), grid)))

if __name__ == "__main__":
    main()