from typing import List
from copy import deepcopy


def pp(grid: list) -> None:
    for y in grid:
        for x in y:
            print(x, end="")
        print()


def selection_filter(grid: list, positions: list) -> int:
    ret = 0
    for pos in positions:
        y, x = pos
        if grid[y][x] == "@":
            ret += 1
    if ret < 4:
        return 1
    return 0


def solve(example: List[str]) -> int:
    ret_val = 0
    grid = []
    for i, line in enumerate(example):
        grid.append([x for x in line])
    fancy_grid = deepcopy(grid)

    for iy, y in enumerate(grid):
        for ix, x in enumerate(y):
            if grid[iy][ix] != "@":
                continue
            positions = [
                (delta_y, delta_x)
                for delta_x in range(ix - 1, ix + 2)
                for delta_y in range(iy - 1, iy + 2)
                if (delta_x, delta_y) != (ix, iy)
                and (delta_x >= 0 and delta_x < len(y))
                and (delta_y >= 0 and delta_y < len(grid))
            ]
            if selection_filter(grid, positions) != 0:
                fancy_grid[iy][ix] = "x"

            ret_val += selection_filter(grid, positions)

    # pp(fancy_grid)
    return ret_val
