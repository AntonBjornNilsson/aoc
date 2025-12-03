from typing import List
from copy import deepcopy


def recr(start: list, saved: list = [], level: int = 12):
    if level == 0:
        return saved
    bank = deepcopy(start)
    bank.sort(reverse=True)

    while p1 := start.index(bank[0]):
        bank.pop(0)
        if p1 <= len(start) - level:
            break
    saved.append(start[p1])
    bank_new = [int(x) for x in start[p1 + 1 : :]]
    return recr(bank_new, saved, level - 1)


def solve(example: List[str]) -> int:
    ret_val = 0
    for i, line in enumerate(example):
        bank = [int(x) for x in line]
        res = recr(bank, [])
        res_int = int("".join([str(x) for x in res]))

        ret_val += res_int
    return ret_val
