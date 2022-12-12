#!/usr/local/env python
from pathlib import Path
from typing import List


with (Path(__file__).parent / "input.txt").open() as text:

    lines = [line.strip() for line in text.read().split("\n") if line]


def solve(init_list: list) -> int:
    inner = 0
    matrix = [[int(y) for y in x] for x in init_list]
    rows = len(matrix)
    cols = len(matrix[0])
    for r_index in range(1, rows - 1):
        for c_index in range(1, cols - 1):
            ups = [matrix[x][c_index] for x in range(0, r_index + 1)]
            downs = [matrix[x][c_index] for x in range(r_index, rows)]
            lefts = [matrix[r_index][x] for x in range(0, c_index + 1)]
            rights = [matrix[r_index][x] for x in range(c_index, cols)]
            downs.reverse()
            rights.reverse()
            if all(ups[-1] > x for x in ups[:-1]):
                inner += 1
                continue
            if all(downs[-1] > x for x in downs[:-1]):
                inner += 1
                continue
            if all(lefts[-1] > x for x in lefts[:-1]):
                inner += 1
                continue
            if all(rights[-1] > x for x in rights[:-1]):
                inner += 1
                continue
    outer = 2 * rows + 2 * cols - 4
    return outer + inner


def find_score(_list: List[int]):
    current = _list.pop()
    local_delta = 0
    while len(_list) > 0:
        local_delta += 1
        if _list[-1] < current:
            _list.pop()
        else:
            break
    return local_delta


def solve2(init_list: list) -> int:
    possible_answers = []
    matrix = [[int(y) for y in x] for x in init_list]
    rows = len(matrix)
    cols = len(matrix[0])
    for r_index in range(1, rows - 1):
        for c_index in range(1, cols - 1):
            ups = [matrix[x][c_index] for x in range(0, r_index + 1)]
            downs = [matrix[x][c_index] for x in range(r_index, rows)]
            lefts = [matrix[r_index][x] for x in range(0, c_index + 1)]
            rights = [matrix[r_index][x] for x in range(c_index, cols)]
            downs.reverse()
            rights.reverse()
            up = find_score(ups)
            down = find_score(downs)
            left = find_score(lefts)
            right = find_score(rights)
            possible_answers.append(up * down * right * left)

    return max(possible_answers)


example = [
    e.strip()
    for e in """30373
25512
65332
33549
35390
""".split(
        "\n"
    )
    if e
]


part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 21
print("Part 1:", solve(lines))

# 652 -
# 1695 correct
part2 = solve2(example)
print("Example part 2:", part2)
assert part2 == 8
print("Part 2:", solve2(lines))

# 287040 correct
