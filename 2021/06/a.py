#!/usr/local/env python
from pathlib import Path
from typing import DefaultDict

with (Path(__file__).parent / "input.txt").open() as text:
    line = text.read()


def solve(init_list: str, days: int) -> int:
    fishes = DefaultDict(lambda: 0)
    for e in init_list.split(","):
        fishes[int(e)] += 1
    count = sum(list(fishes.values()))
    for day in range(days):
        cur_f = fishes[day]
        fishes[day + 9] += cur_f
        fishes[day + 7] += cur_f
        count += cur_f
    return count


example = """3,4,3,1,2"""


assert 26 == solve(example, 18)
assert 5934 == solve(example, 80)
assert solve(example, 256) == 26984457539

print("Part 1:", solve(line, 80))
print("Part 2:", solve(line, 256))
