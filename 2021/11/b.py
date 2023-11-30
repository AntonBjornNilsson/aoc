#!/usr/local/env python
from pathlib import Path
from typing import DefaultDict

with (Path(__file__).parent / "input.txt").open() as text:
    lines = [line.strip() for line in text.read().split("\n") if line]


def gen():
    for x in range(10):
        for y in range(10):
            yield x, y


def all_plus_one(matrix):
    for x, y in gen():
        matrix[x][y] += 1


def check_sync(matrix):
    for x, y in gen():
        if matrix[x][y] != 0:
            return False
    return True


def clear_flashed(matrix):
    for x, y in gen():
        if matrix[x][y] < 0:
            matrix[x][y] = 0


def flash_region(matrix, x, y):
    x_lower = max(0, x - 1)
    y_lower = max(0, y - 1)
    x_upper = min(9, x + 1) + 1
    y_upper = min(9, y + 1) + 1
    flashes = 1
    matrix[x][y] = -1
    c = len(list(range(x_lower, x_upper))) * len(list(range(y_lower, y_upper)))
    calls = 0
    for _x in range(x_lower, x_upper):
        for _y in range(y_lower, y_upper):
            calls += 1

            if matrix[_x][_y] >= 0:
                matrix[_x][_y] += 1

            if matrix[_x][_y] > 9:
                flashes += flash_region(matrix, _x, _y)
    assert c == calls, f"calls was not correct {c} != {calls}"
    return flashes


def flash(matrix):
    count = 0
    for x, y in gen():
        cur = matrix[x][y]
        if cur > 9:
            count += flash_region(matrix, x, y)
    return count


def solve(init_list: list, _range: int) -> int:
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    for x, y in gen():
        matrix[x][y] = int(init_list[x][y])
    count = 0
    for _ in range(_range):
        all_plus_one(matrix)
        count += flash(matrix)
        clear_flashed(matrix)
    for l in matrix:
        print(l)
    return count


def solve2(init_list: list, _range: int = 10000) -> int:
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    for x, y in gen():
        matrix[x][y] = int(init_list[x][y])
    count = 0
    for step in range(_range):
        all_plus_one(matrix)
        count += flash(matrix)
        clear_flashed(matrix)
        if check_sync(matrix):
            return step + 1
    for l in matrix:
        print(l)
    return count


example = [
    e.strip()
    for e in """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".split(
        "\n"
    )
    if e
]


part2 = solve2(example, 196)
print("Example part 2:", part2)
assert part2 == 195
print("Part 2:", solve2(lines))
