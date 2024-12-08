left = []
right = []
sum = 0
counter = 0
multSum = 0
finalSum = 0

with open("/Users/oscarpenn/Desktop/VSCODE PROJECTS/PYTHON/ADVENTOFCODE/advent-1/input.txt") as f:
    content = f.read().split()
    for i in range(len(content)):
        if i % 2 == 0:
            left.append(content[i])
        else:
            right.append(content[i])

    sortedLeft = sorted(left)
    sortedRight = sorted(right)

    print(len(sortedLeft))
    print(len(sortedRight))

    for i in range(len(sortedLeft)):
        difference = abs(int(sortedLeft[i]) - int(sortedRight[i]))
        sum += difference

    print(sum)

    for i in range(len(sortedLeft)):
        counter = 0
        for j in range(len(sortedRight)):
            if sortedLeft[i] == sortedRight[j]:
                counter += 1
        currentNum = int(sortedLeft[i])
        multSum = currentNum * counter
        finalSum += multSum

    print(finalSum)