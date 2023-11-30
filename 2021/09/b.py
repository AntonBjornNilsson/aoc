#!/usr/local/env python
from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as text:
    lines = [line.strip() for line in text.read().split("\n") if line]


def solve(init_list: list) -> int:
    matrix = []
    for i in init_list:
        matrix.append([int(x) for x in i])
    count = []
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            cur = matrix[row][col]
            sides = []
            if col > 0:
                sides.append(matrix[row][col - 1])
            if col < cols - 1:
                sides.append(matrix[row][col + 1])
            if row > 0:
                sides.append(matrix[row - 1][col])
            if row < rows - 1:
                sides.append(matrix[row + 1][col])
            if all([cur < s for s in sides]):
                count.append((row, col))
    return count


def check(matrix, row, col, rows, cols, global_basin):
    cur = matrix[row][col]
    cur_cells = []
    if col > 0:
        left = matrix[row][col - 1]
        if cur < left and left != 9 and (row, col - 1) not in global_basin:
            cur_cells.append((row, col - 1))
    if col < cols - 1:
        right = matrix[row][col + 1]
        if cur < right and right != 9 and (row, col + 1) not in global_basin:
            cur_cells.append((row, col + 1))
    if row > 0:
        up = matrix[row - 1][col]
        if cur < up and up != 9 and (row - 1, col) not in global_basin:
            cur_cells.append((row - 1, col))
    if row < rows - 1:
        down = matrix[row + 1][col]
        if cur < down and down != 9 and (row + 1, col) not in global_basin:
            cur_cells.append((row + 1, col))
    return cur_cells


def solve2(init_list: list) -> int:
    matrix = []
    for i in init_list:
        matrix.append([int(x) for x in i])
    count = []
    rows = len(matrix)
    cols = len(matrix[0])
    lowest: list = solve(init_list)
    for row, col in lowest:
        cur = matrix[row][col]
        if cur != 9:
            basin = [(row, col)]
            global_basin = [(row, col)]
            c = 0
            while basin:
                x, y = basin.pop(0)
                c += 1
                cells = check(matrix, x, y, rows, cols, global_basin)
                basin.extend(cells)
                global_basin.extend(cells)
            count.append(c)

    from functools import reduce

    return reduce((lambda x, y: x * y), sorted(count, reverse=True)[0:3])


example = [
    e.strip()
    for e in """2199943210
3987894921
9856789892
8767896789
9899965678
""".split(
        "\n"
    )
    if e
]


part2 = solve2(example)
print("Example part 2:", part2)
assert part2 == 1134
print("Part 2:", solve2(lines))
