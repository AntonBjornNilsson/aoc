import re
from typing import List
from regex import find_all_int
import operator
from functools import reduce


def solve(example: List[str]) -> int:
    ret_val = 0
    problems_grid = []
    for i, line in enumerate(example[:-1]):
        problems_grid.append([int(x) for x in find_all_int(line)])
    signs = [
        operator.add if x == "+" else operator.mul
        for x in re.findall(r"\S", example[-1])
    ]

    for i, op in enumerate(signs):
        curr = [x[i] for x in problems_grid]
        ret_val += reduce(op, curr)

    return ret_val
