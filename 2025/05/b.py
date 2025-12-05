from copy import deepcopy
from typing import List


def solve(example: List[str]) -> int:
    ret_val = []
    hits_list = []
    for i, line in enumerate(example):
        if "-" in line:
            hits_list.append([int(x) for x in line.split("-")])
            continue

    s_range = sorted(hits_list, key=lambda x: x[0])
    s, e = s_range[0]

    for start, end in s_range:
        if start == s and e == end:
            s, e = start, end
        if start <= e + 1:
            e = max(e, end)
        else:
            ret_val.append((s, e))
            s, e = start, end

    ret_val.append((s, e))

    return sum(bottom_bound - upper_bound + 1 for upper_bound, bottom_bound in ret_val)


# 304174648129831 low
# 354143734113772 correct
