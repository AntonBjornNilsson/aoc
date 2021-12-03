#!/usr/local/env python
import math
from pathlib import Path

each_line_is_bool = False
with (Path(__file__).parent / "input.txt").open() as text:
    try:
        lines = [ int(line) for line in text.readlines() if line]
        each_line_is_bool = True
    except ValueError:
        lines = [ line.strip() for line in text.readlines() if line]


def solve(init_list: list) -> int:
    return 0


# def solve2(init_list: list) -> int:



example = [ e.strip() for e in """<example_string>""".split("\n") ]
if each_line_is_bool:
    example = [ int(e) for e in example if e]

part1 = solve(example)
print(part1)
assert part1 == <answer_string>
print("Part 1:", part1)
