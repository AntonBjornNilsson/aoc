#!/usr/local/env python
from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as text:

    lines = [line.strip() for line in text.read().split("\n") if line]


def ascii_conversion(c: str):
    if c.islower():
        return ord(c) - 96
    return ord(c) - 38


def solve(init_list: list) -> int:
    tot = 0
    for line in init_list:
        l = len(line)
        half = int(l / 2)
        first = line[:half]
        second = line[half:]
        for f in set(first):
            if f in second:
                tot += ascii_conversion(f)
    return tot


# def solve2(init_list: list) -> int:


example = [
    e.strip()
    for e in """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".split(
        "\n"
    )
    if e
]


part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 157
print("Part 1:", solve(lines))
