#!/usr/local/env python
from pathlib import Path
from typing import DefaultDict

with (Path(__file__).parent / "input.txt").open() as text:

    lines = [ line.strip() for line in text.read().split("\n") if line]


def solve(init_list: list) -> int:
    coords = [[0 for x in range(1000)] for x in range(1000)]
    for line in init_list:
        start_coords = line.split(" -> ")[0].split(",")
        start_coords = [int(e) for e in start_coords]
        end_coords = line.split(" -> ")[1].split(",")
        end_coords = [int(e) for e in end_coords]
        if start_coords[0] == end_coords[0] or start_coords[1] == end_coords[1]:
            x1 = min(start_coords[0], end_coords[0])
            x2 = max(start_coords[0], end_coords[0])
            y1 = min(start_coords[1], end_coords[1])
            y2 = max(start_coords[1], end_coords[1])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    coords[y][x] += 1

    total = 0
    for c in coords:
        for k in c:
            if k >= 2:
                total += 1
    return total

# def solve2(init_list: list) -> int:



example = [ e.strip() for e in """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".split("\n") if e ]


part1 = solve(example)
print("Example part 1", part1)
assert part1 == 5
print("Part 1:", solve(lines))
