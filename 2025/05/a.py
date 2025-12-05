from typing import List


def solve(example: List[str]) -> int:
    ret_val = set()
    hits_list = []
    search = []
    for i, line in enumerate(example):
        if not line:
            continue
        if "-" in line:
            hits_list.append([int(x) for x in line.split("-")])
            continue
        search.append(int(line))

    for hit in hits_list:
        low, high = hit
        for s in search:
            if s >= low and s <= high:
                # print('hit for', s, 'on span', low, '-', high)
                ret_val.add(s)

    return len(ret_val)
