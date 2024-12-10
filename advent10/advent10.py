from collections import defaultdict

with open("ADVENTOFCODE/advent10/input.txt") as f:
    lines = f.read().splitlines()

# Create a dictionary of coordinates and heights
grid = {}
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        grid[x + y * 1j] = int(char)

# Create list of trailheads and neighbourOffsets, initialise graph
trailheads = [key for key, value in grid.items() if value == 0]
neighboursOffsets = [1+0j, -1+0j, 0+1j, 0-1j]
graph = defaultdict(list)

# Create the graph
for key, height in grid.items():
    for offset in neighboursOffsets:
        neighbour = key + offset
        if neighbour in grid and grid[neighbour] == height + 1:
            graph[key].append(neighbour)


# Find the 9's from the trailheads using a depth first search and add the coords to a set
def find_nines_from_trailheads():
    count = 0
    reachable_nines = set()

    def dfs(node, visited):
        if grid[node] == 9:
            reachable_nines.add(node)
            return
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour, visited)

    for trailhead in trailheads:
        reachable_nines = set()
        dfs(trailhead, set())
        print(reachable_nines)
        count += len(reachable_nines)

    return count

reachable_nines = find_nines_from_trailheads()
print(reachable_nines)
