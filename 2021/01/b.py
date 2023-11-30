#!/usr/local/env python

import math
from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as text:
    try:
        lines = [int(line) for line in text.readlines() if line]
        each_line_is_bool = True
    except ValueError:
        lines = [line for line in text.readlines() if line]
        each_line_is_bool = False


def solve(init_list: list) -> int:
    count = -1
    last = 0
    for y in init_list:
        if y > last:
            count += 1
        last = y
    return count


def solve2(init_list: list) -> int:
    count = -1
    last = 0

    for _x in range(len(init_list)):
        x1 = init_list[_x]
        x2 = 0
        x3 = 0
        try:
            x2 = init_list[_x + 1]
        except:
            pass
        try:
            x3 = init_list[_x + 2]
        except:
            pass
        if (x1 + x2 + x3) > last:
            count += 1
        last = x1 + x2 + x3
    return count


example = """199
200
208
210
200
207
240
269
260
263
""".split(
    "\n"
)
if each_line_is_bool:
    example = [int(e) for e in example if e]


part1 = solve(example)
assert part1 == 7
print("Part 1:", part1)

part2 = solve2(example)
assert part2 == 5
print("Part 2:", part2)
