with open("ADVENTOFCODE/advent9/input.txt") as f:
    input = list(f.read())

# Create list of id numbers
id = []
idCount = -1
for i, item in enumerate(input):
    if i % 2 == 0:
        id.extend([int(i) // 2] * int(item))
        idCount += 1
    else:
        id.extend(['.'] * int(item))

# Compact id list


# Calculate checksum
checkSum = 0
for position, block in enumerate(id):
    if block != '.':
        checkSum += position * block

print(id)
print(checkSum)