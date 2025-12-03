from typing import List


def solve(example: List[str]) -> int:
    ret_val = 0
    for i, line in enumerate(example):
        bank = [int(x) for x in line]
        bank2 = [int(x) for x in line]
        bank.sort(reverse=True)

        while p1 := bank2.index(bank[0]):

            bank.pop(0)
            if p1 != len(line) - 1:
                break
        bank_new = [int(x) for x in line[p1 + 1 : :]]

        ret_val += (bank2[p1] * 10) + max(bank_new)
    return ret_val
