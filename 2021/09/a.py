#!/usr/local/env python
from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as text:

    lines = [line.strip() for line in text.read().split("\n") if line]


def solve(init_list: list) -> int:
    matrix = []
    for i in init_list:
        matrix.append([int(x) for x in i])
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        print("---")
        for col in range(cols):
            cur = matrix[row][col]
            sides = []
            print(cur, col, cols)
            if col > 0:
                sides.append(matrix[row][col - 1])
            if col < cols - 1:
                sides.append(matrix[row][col + 1])
            if row > 0:
                sides.append(matrix[row - 1][col])
            if row < rows - 1:
                sides.append(matrix[row + 1][col])
            if row == 0 and col == 9:
                print("found", row, col, cur)
            if all([cur < s for s in sides]):
                count += cur + 1
                print("found", row, col, cur)
    return count


# def solve2(init_list: list) -> int:


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


part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 15
print("Part 1:", solve(lines))
