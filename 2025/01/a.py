from typing import List


def solve(example: List[str]) -> int:
    ret_val = 0
    point = 50
    zeros = 0
    for i, line in enumerate(example):
        r, dist = line[0], int(line[1:])
        dist = dist % 100
        if r == "L":
            point = point - dist + 100

        if r == "R":
            point = abs(point + dist)

        if point >= 100:
            point = point % 100

        if point == 0:
            ret_val += 1

    return ret_val
