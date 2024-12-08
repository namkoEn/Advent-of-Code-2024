# PART 1
with open("python/ADVENTOFCODE/advent6/input.txt") as f:
    file = f.read().strip().split('\n')

global map
map = [list(row) for row in file]

global row, column
row = column = -1
for i, r in enumerate(map):
    for j, value in enumerate(r):
        if value == "^":
            column = i
            row = j
            break

def rotate(direction):
    if direction == "y+":
        return "x+"
    elif direction == "x+":
        return "y-"
    elif direction == "y-":
        return "x-"
    else:
        return "y+"

def moveUp():
    global row, column, direction, flag
    map[column][row] = "X"
    if column - 1 < 0:
        flag = False
    elif map[column - 1][row] == '#':
        direction = rotate(direction)
    else:
        column -= 1
        map[column][row] = "^"

def moveDown():
    global row, column, direction, flag
    map[column][row] = "X"
    if column + 1 >= len(map):
        flag = False
    elif map[column + 1][row] == '#':
        direction = rotate(direction)
    else:
        column += 1
        map[column][row] = "v"

def moveRight():
    global row, column, direction, flag
    map[column][row] = "X"
    if row + 1 >= len(map[column]):
        flag = False
    elif map[column][row + 1] == '#':
        direction = rotate(direction)
    else:
        row += 1
        map[column][row] = ">"

def moveLeft():
    global row, column, direction, flag
    map[column][row] = "X"
    if row - 1 < 0:
        flag = False
    elif map[column][row - 1] == '#':
        direction = rotate(direction)
    else:
        row -= 1
        map[column][row] = "<"

def moveGuard(direction):
    if direction == "y+":
        moveUp()
    elif direction == "y-":
        moveDown()
    elif direction == "x+":
        moveRight()
    elif direction == "x-":
        moveLeft()

direction = "y+"
flag = True
while flag:
    moveGuard(direction)

count = 0
for i, r in enumerate(map):
    for j, value in enumerate(r):
        if value == "X":
            count += 1

print(f"Number of X's: {count}")