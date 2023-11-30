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
    x = 0
    y = 0
    for e in init_list:
        if "forward " in e:
            x += int(e[-1])
        if "up " in e:
            y += int(e[-1])
        if "down " in e:
            y -= int(e[-1])
    return x * abs(y)


def solve2(init_list: list) -> int:
    hor = 0
    aim = 0
    depth = 0
    for e in init_list:
        if "forward " in e:
            hor += int(e[-1])
            depth += aim * int(e[-1])
        if "up " in e:
            aim += int(e[-1])
        if "down " in e:
            aim -= int(e[-1])
    return hor * abs(depth)


example = """forward 5
down 5
forward 8
up 3
down 8
forward 2
""".split(
    "\n"
)
if each_line_is_bool:
    example = [int(e) for e in example if e]

part1 = solve(example)
assert part1 == 150
print("Part 1:", part1)

part2 = solve2(example)
assert part2 == 900
print("Part 2:", part2)
