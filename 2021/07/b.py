#!/usr/local/env python
from pathlib import Path

each_line_is_bool = False
with (Path(__file__).parent / "input.txt").open() as text:
    try:
        lines = [int(line) for line in text.read().split(",") if line]
        each_line_is_bool = True
    except ValueError:
        lines = [line.strip() for line in text.read() if line]


def solve(init_list: list) -> int:
    mx = max(init_list)
    run = []
    for x in range(0, mx):
        cost = 0
        for i in init_list:
            cost += max(i, x) - min(i, x)
            # print(f"Move from {i} to {position}: {max(i, position)- min(i, position)} fuel")
        run.append(cost)
    print(run.index(min(run)))
    return min(run)


def solve2(init_list: list) -> int:
    mx = max(init_list)
    run = []
    for position in range(0, mx):
        cost = 0
        for i in init_list:
            this_cost = sum(range(0, max(i, position) - min(i, position) + 1))
            cost += this_cost
            # print(f"Move from {i} to {position}: {this_cost} fuel")
        run.append(cost)
    return min(run)


example = [e.strip() for e in """16,1,2,0,4,2,7,1,2,14""".split(",") if e]
if each_line_is_bool:
    example = [int(e) for e in example if e]


part2 = solve2(example)
print("Example part 2:", part2)
assert part2 == 168
print("Part 2:", solve2(lines))
