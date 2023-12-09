from typing import List
from regex import find_all_int


def recr(inputs: List[int]) -> List[int]:
    ret_vals: List[int] = []
    if all(x == 0 for x in inputs):
        return 0
    new_vals = [inputs[x + 1] - inputs[x] for x in range(len(inputs) - 1)]
    return recr(new_vals) + inputs[-1]


def solve(example: List[str]) -> int:
    ret_val = 0
    for i, line in enumerate(example):
        seq = [int(x) for x in line.split(" ")]
        res = recr(seq)
        ret_val += res

    return ret_val
