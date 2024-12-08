from itertools import product
import operator

def concat(a, b):
    return int(str(a) + str(b))

total = 0
operators = {operator.add, operator.mul, concat}

with open("python/ADVENTOFCODE/advent7/input.txt") as input:
    for line in input:
        (result, numbers) = int(line.split(":")[0]), [int(x) for x in line.split(":")[1].strip().split(" ")]

        op_order_variations = list(product(operators, repeat=len(numbers)-1))

        for op_order in op_order_variations:
            op_order_result = numbers[0]
            for i, op in enumerate(op_order):
                op_order_result = op(op_order_result, numbers[i+1])
  
            if op_order_result == result:
                total += result
                break

print(total)