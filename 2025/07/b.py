from typing import List
from functools import cache

grid = []


@cache
def recr(pos: tuple[int, int]) -> int:
    ret = 0
    if pos[0] + 1 == len(grid) - 1:
        return 1
    for iy in range(pos[0] + 1, len(grid)):
        if grid[iy][pos[1]] == "^":

            for new in [(iy, pos[1] - 1), (iy, pos[1] + 1)]:
                ret += recr(new)

            return ret
    return ret + 1


def solve(example: List[str]) -> int:
    local = []
    start = [0, 0]

    for iy, line in enumerate(example):
        local.append([char for char in line])
        if "S" in line:
            start = (iy, line.index("S"))

    global grid
    grid = local
    ret = recr(start)

    return ret


# 25592971184998 correct
