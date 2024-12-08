def safe_level(line):
    data = [int(n) for n in line.split()]
    up = all(a < b for a, b in zip(data, data[1:]))
    dn = all(a > b for a, b in zip(data, data[1:]))
    dif = all(abs(a - b) <= 3 for a, b in zip(data, data[1:]))
    return (up or dn) and dif

def count_safe_reports(filename, func=safe_level):
    with open(filename) as fh:
        return sum(func(line) for line in fh.readlines())

print("Test:  ", count_safe_reports("/Users/oscarpenn/Desktop/VSCODE PROJECTS/PYTHON/ADVENTOFCODE/advent-2/input.txt"), safe_level)
print("Part 1:", count_safe_reports("/Users/oscarpenn/Desktop/VSCODE PROJECTS/PYTHON/ADVENTOFCODE/advent-2/input.txt"), safe_level)

def safe_dampener(line):
    if safe_level(line):
        return True
    else:
        data = line.split()
        return any(
            safe_level(' '.join(data[:i] + data[i + 1:]))
            for i in range(len(data))
        )

print("Test:  ", count_safe_reports("/Users/oscarpenn/Desktop/VSCODE PROJECTS/PYTHON/ADVENTOFCODE/advent-2/input.txt", safe_dampener))
print("Part 2:", count_safe_reports("/Users/oscarpenn/Desktop/VSCODE PROJECTS/PYTHON/ADVENTOFCODE/advent-2/input.txt", safe_dampener))