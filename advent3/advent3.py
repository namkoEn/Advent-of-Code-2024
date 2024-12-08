import re
productSum = 0
flag = True

with open("/Users/oscarpenn/Desktop/VSCODE PROJECTS/PYTHON/ADVENTOFCODE/advent-3/input.txt") as f:
    fileList = f.read()
    operationList = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", fileList)

for operation in operationList:
    if operation == "do()":
        flag = True
    elif operation == "don't()":
        flag = False
    elif "mul" in operation and flag is True:
        num = re.findall(r'\b\d+\b', operation)
        product = int(num[0]) * int(num[1])
        productSum += product

print(productSum)
