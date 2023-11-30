#!/usr/local/env python
import math
from pathlib import Path
import re
from typing import Dict, Tuple
from collections import defaultdict


with (Path(__file__).parent / "input.txt").open() as text:
    lines = [line.strip() for line in text.read().split("\n") if line]


def print_coverage(mapping: Dict[Tuple[int, int], Tuple[int, int]], search: int):
    largest_row = sorted(
        [x[0] for x in mapping.keys()] + [x[0] for x in mapping.values()]
    )[-1]
    largest_col = sorted(
        [x[1] for x in mapping.keys()] + [x[1] for x in mapping.values()]
    )[-1]
    smallest_row = sorted(
        [x[0] for x in mapping.keys()] + [x[0] for x in mapping.values()]
    )[0]
    smallest_col = sorted(
        [x[1] for x in mapping.keys()] + [x[1] for x in mapping.values()]
    )[0]
    print(smallest_row, largest_row)
    print(smallest_col, largest_col)
    beacons = list(mapping.values())
    sensors = list(mapping.keys())
    # fancy_row = (largest_row // 10) +1
    grid = [
        ["." for _ in range(smallest_col, largest_col)]
        for _ in range(smallest_row, largest_row)
    ]
    # grid = defaultdict(lambda: defaultdict(lambda: []))
    # print(grid)
    print("loaded")
    # for row in range(smallest_row, largest_row):
    #     # print(grid[row])
    #     # print(f"{row}".ljust(fancy_row), end="")
    #     for col in range(smallest_col, largest_col):
    #         if (col, row) in sensors:
    #             # print("S", end="")
    #             grid[row].append("S")
    #         elif (col, row) in beacons:
    #             # print("B", end="")
    #             grid[row].append("B")
    #         # else:
    #             # print(".", end="")
    #             # grid[row].append(".")
    #     # print()

    # print("--------------------")
    # y_extras = defaultdict(lambda: [])
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
        # print(abs(sx - bx), delta_x, abs(sy - by), delta_y, will_intersect)
        if not will_intersect:
            continue
        # print("sensor", sx, sy)
        # print("beacon", bx, by)
        # print(sy, by, "delta", delta_y, "will intersect")
        # print(delta_x + delta_y)
        expand_index = delta_x + delta_y + 1

        # y = search
        for y in range(sy - delta_y + 1, sy + delta_y):
            if y < 0:
                continue
            # if y != search:
            #     continue
            delta_y = abs(abs(sy - y) - expand_index)
            # print("y loop", sy, y, delta_y)
            for x in range(sx - delta_y + 1, sx + delta_y):
                if x < 0:
                    continue
                curr = (x, y)
                # print(curr, beacon)
                if curr == beacon:
                    print("found beacon")
                    continue
                elif curr in sensors:
                    continue
                else:
                    try:
                        print(y, x)
                        grid[y][x] = "#"
                    except:
                        pass
        # if expand_index > 20:
        #     break
        # expand_index += 1
    print(len(grid))
    print(len(grid[0]))
    for i in range(len(grid)):
        # print(row)
        for col in range(len(grid[i])):
            print(grid[i][col], end="")
        print()
    # for i, row in enumerate(grid):
    #     print(f"{i}".ljust(fancy_row), end="")
    #     for col in row:
    #         print(col, end="")
    #     print()
    # print(grid[search], y_extras[search])

    return grid


def solve2(init_list: list, search=10) -> int:
    sensor_2_beacon = {}
    for line in init_list:
        sx, sy, bx, by = re.findall(r"\d+", line)
        sensor_2_beacon[(int(sx), int(sy))] = (int(bx), int(by))
    _, beacons = print_coverage(sensor_2_beacon, search)

    for beacon in beacons:

        res = beacon[0] * 4000000 + beacon[1]
        print(beacon, res)

    return beacons


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


part2 = solve2(example)
print("Example part 2:", part2)
assert part2 == 56000011
# print("Part 1:", solve(lines, 2000000))
