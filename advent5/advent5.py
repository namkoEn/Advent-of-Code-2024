from collections import defaultdict, deque

with open("python/ADVENTOFCODE/advent5/input.txt") as f:
    file = f.read().strip().split('\n')

tempIdx = file.index('')
ordering = file[:tempIdx]
puzzleInput = [list(map(int, entry.split(','))) for entry in file[tempIdx+1:]]

rules = defaultdict(list)
for item in ordering:
    before, after = map(int, item.split('|'))
    rules[before].append(after)

def is_valid_update(update):
    position = {page: i for i, page in enumerate(update)}
    for before, afters in rules.items():
        if before in position:
            for after in afters:
                if after in position and position[before] > position[after]:
                    return False
    return True

def topological_sort(pages, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for page in pages:
        in_degree[page] = 0
    for before in pages:
        for after in rules[before]:
            if after in pages:
                graph[before].append(after)
                in_degree[after] += 1

    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_pages = []
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages

middle_sum = 0
for update in puzzleInput:
    if not is_valid_update(update):
        sorted_update = topological_sort(update, rules)
        middle_sum += sorted_update[len(sorted_update) // 2]

print(middle_sum)