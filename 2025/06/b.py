import re
from typing import List
from regex import find_all_int
import operator
from functools import reduce


def solve(example: List[str]) -> int:
    ret_val = 0
    op = operator.add
    saved = []
    example = [x + " " for x in example]
    for yi in range(max([len(x) for x in example]) - 1):
        cols = []
        o = example[len(example) - 1][yi]
        if o == "*":
            op = operator.mul
        if o == "+":
            op = operator.add

        for xi in range(len(example) - 1):
            c = example[xi][yi]
            if c != " ":
                cols.append(c)
        if cols == [] or "\n" in cols:
            value = reduce(op, saved)
            ret_val += value
            saved = []
        else:
            saved.append(int("".join(cols)))

    return ret_val


# remove line.strip() from parser to make it work
# to sleepy to make it nice
