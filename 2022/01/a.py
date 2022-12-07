#!/usr/local/env python
from pathlib import Path

each_line_is_bool = False
with (Path(__file__).parent / "input.txt").open() as text:
    lines = [ line for line in text.read().split("\n")]


def solve(init_list: list) -> int:
    tot_list = [0]
    for line in init_list:
        if not line:
            print("space")
            tot_list.append(0)

        else:
            print("no_space")
            tot_list[-1] += int(line)
    print(tot_list)
    return max(tot_list)


# def solve2(init_list: list) -> int:



example = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".split("\n")
if each_line_is_bool:
    example = [ int(e) for e in example if e]

part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 24000
print("Part 1:", solve(lines))
