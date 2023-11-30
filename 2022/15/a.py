#!/usr/local/env python
import math
from pathlib import Path
import re
from typing import Dict, Tuple
from collections import defaultdict


with (Path(__file__).parent / "input.txt").open() as text:
    lines = [line.strip() for line in text.read().split("\n") if line]


def print_coverage(mapping: Dict[Tuple[int, int], Tuple[int, int]], search: int):

    sensors = list(mapping.keys())

    grid = defaultdict(lambda: defaultdict(lambda: 0))

    for sx, sy in sensors:
        bx, by = mapping[(sx, sy)]
        beacon = mapping[(sx, sy)]

        delta_y = abs(sy - by)
        delta_x = abs(sx - bx)

        will_intersect = (
            sy + delta_y >= search
            and sy <= search
            or sy - delta_y <= search
            and sy >= search
        ) or (
            sy + delta_x >= search
            and sy <= search
            or sy - delta_x <= search
            and sy >= search
        )

        if not will_intersect:
            continue

        expand_index = delta_x + delta_y + 1
        y = search

        delta_y = abs(abs(sy - y) - expand_index)

        for x in range(sx - delta_y + 1, sx + delta_y):
            curr = (x, y)
            if curr == beacon:
                continue
            elif curr in sensors:
                continue
            else:
                grid[y][x] += 1

    return grid


def solve(init_list: list, search=10) -> int:
    sensor_2_beacon = {}
    for line in init_list:
        sx, sy, bx, by = re.findall(r"\d+", line)
        sensor_2_beacon[(int(sx), int(sy))] = (int(bx), int(by))
    grid = print_coverage(sensor_2_beacon, search)
    amount = len(grid[search])

    return amount


example = [
    e.strip()
    for e in """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
""".split(
        "\n"
    )
    if e
]

part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 26
print("Part 1:", solve(lines, 2000000))

# 5147333 Correct
