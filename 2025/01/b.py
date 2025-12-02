from typing import List


def solve(example: List[str]) -> int:
    ret_val = 0
    point = 50

    for i, line in enumerate(example):
        r, dist = line[0], int(line[1:])

        if r == "L":
            point = point - dist

        if r == "R":
            point = point + dist

        ret_val += abs(point // 100)
        point = abs(point % 100)

        print(ret_val, point, dist, line)
    print(ret_val)
    return ret_val
