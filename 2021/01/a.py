#!/usr/local/env python

import math
from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as text:
    try:
        lines = [ int(line) for line in text.readlines() if line]
        each_line_is_bool = True
    except ValueError:
        lines = [ line for line in text.readlines() if line]
        each_line_is_bool = False

def solve(init_list: list) -> int:
    count = -1
    last = 0
    for y in init_list:
        if y > last:
            count += 1
        last = y
    return count

# def solve2(init_list: list) -> int:

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
""".split("\n")
if each_line_is_bool:
    example = [ int(e) for e in example if e]


part1 = solve(example)
assert part1 == 7
print("Part 1:", part1)
