with open("ADVENTOFCODE/advent8/input.txt") as f:
    file = f.read().split()

# Create 2d array of input
map = [list(row) for row in file]

# Create list of all different antennas
antennas = []
for row in map:
    for item in row:
        if item != '.' and item not in antennas:
            antennas.append(item)

# Create a boolean 2d array to store where antinodes are
boolMap = [[False for _ in range(len(map[0]))] for _ in range(len(map))]

# Create dictionary and add coordinates of each antenna
antennaPositions = {antenna: [] for antenna in antennas}
for i, row in enumerate(map):
    for j, item in enumerate(row):
        if item != '.':
            antennaPositions[item].append((i, j))

# Calculate the differences between antennas, find antinodes, and add them to the set
antinodes = set()
for antenna in antennas:
    currentAntennaList = antennaPositions.get(antenna)

    for i in range(len(currentAntennaList)):
        x1, y1 = currentAntennaList[i]
        for j in range(i + 1, len(currentAntennaList)):
            x2, y2 = currentAntennaList[j]
            dx, dy = x2 - x1, y2 - y1
            firstAntinode = x1 - dx, y1 - dy    
            secondAntinode = x2 + dx, y2 + dy

            # Function to check if a coordinate is within bounds
            def is_in_bounds(x, y, width, height):
                return 0 <= x < width and 0 <= y < height

            while is_in_bounds(firstAntinode[0], firstAntinode[1], len(map), len(map[0])):
                antinodes.add(firstAntinode)
                firstAntinode = (firstAntinode[0] - dx, firstAntinode[1] - dy)

            while is_in_bounds(secondAntinode[0], secondAntinode[1], len(map), len(map[0])):
                antinodes.add(secondAntinode)
                secondAntinode = (secondAntinode[0] + dx, secondAntinode[1] + dy)

# Add all antenna positions as antinodes
for antenna, positions in antennaPositions.items():
    for pos in positions:
        antinodes.add(pos)

# Count the total number of antinodes
count = len(antinodes)

print(count)