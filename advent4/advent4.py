target = "XMAS"

with open("PYTHON/ADVENTOFCODE/advent-4/input.txt") as f:
    data = f.readlines()

height, width = len(data), len(data[0]) - 1
grid = {(y, x):data[y][x] for y in range(height) for x in range(width)}

surrItems = [(dy, dx) for dy in [-1, 0, 1] for dx in [-1, 0, 1] if dx != 0 or dy != 0]
count = 0
for y, x in grid:
    for dy, dx in surrItems:
        itemFound = "".join(grid.get((y+dy*i, x+dx*i),"") for i in range(len(target)))
        if itemFound == target:
            count += 1

print(count)

count = 0
for y, x in grid:
    if grid[y, x] == "A":
        positive = grid.get((y-1, x-1),"") + grid.get((y+1, x+1),"")
        negative = grid.get((y-1, x+1),"") + grid.get((y+1, x-1),"")
        if {positive, negative} <= {"SM", "MS"}:
            count += 1

print(count)