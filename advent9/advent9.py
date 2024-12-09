with open("ADVENTOFCODE/advent9/input.txt") as f:
    input = list(f.read())

# Create list of id numbers
id = []
for i, item in enumerate(input):
    if i % 2 == 0:
        id.extend([int(i) // 2] * int(item))
    else:
        id.extend(['.'] * int(item))

# Compact id list
for i in range(len(id) - 1):
    if id[i] == '.':
        for j in range(len(id) - 1, i, -1):
            if id[j] != '.':
                id[i] = id[j]
                id[j] = '.'
                break

# Calculate checksum
checkSum = 0
for position, block in enumerate(id):
    if block != '.':
        checkSum += position * block

print(id)
print(checkSum)