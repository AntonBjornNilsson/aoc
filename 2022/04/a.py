#!/usr/local/env python
from pathlib import Path


with (Path(__file__).parent / "input.txt").open() as text:
    lines = [ line.strip() for line in text.read().split("\n") if line]

def parse(xx: str) -> str:
    s_start, s_stop = [int(x) for x in xx.split("-")]
    return list(range(s_start, s_stop + 1))


def solve(init_list: list) -> int:
    tot = 0
    for i in range(len(init_list)):
        first, second = init_list[i].split(",")
        fr = parse(first)
        sr = parse(second)
        if all(x in sr for x in fr):
            tot += 1
        elif all(x in fr for x in sr):
            tot += 1
    return tot


# def solve2(init_list: list) -> int:



example = [ e.strip() for e in """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".split("\n") if e ]


part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 2
print("Part 1:", solve(lines))

# 618 +
# 584 +
# 560 forgot the el in elif