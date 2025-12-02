from typing import List
import numpy as np


def eval_load(max_val: int, line: list, index: int = 0) -> int:
    try:
        stopper = line.index("#")
    except ValueError:
        stopper = len(line)
    count = [max_val - index - x for x in range(line[:stopper].count("O"))]
    if stopper != len(line) and "O" in line[stopper + 1 :]:
        return sum(count) + eval_load(
            max_val, line[stopper + 1 :], index=stopper + index + 1
        )
    return sum(count)


def solve(example: List[str]) -> int:
    ret_val = 0
    temp = np.array([list(row) for row in example])
    grid = np.transpose(temp).tolist()
    for i, line in enumerate(grid):
        line: list
        ret_val += eval_load(len(line), line)

    return ret_val
