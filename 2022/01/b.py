#!/usr/local/env python
from pathlib import Path

each_line_is_bool = False
with (Path(__file__).parent / "input.txt").open() as text:
    lines = [ line for line in text.read().split("\n")]


def solve(init_list: list) -> int:
    tot_list = [0]
    for line in init_list:
        if not line:
            tot_list.append(0)

        else:
            tot_list[-1] += int(line)
    return max(tot_list)


def solve2(init_list: list) -> int:
    tot_list = [0]
    for line in init_list:
        if not line:
            tot_list.append(0)

        else:
            tot_list[-1] += int(line)
    ret = 0
    for _ in range(3):
        inter = max(tot_list)
        tot_list.remove(inter)
        ret += inter
    return ret


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

part2 = solve2(example)
print('Example part 2:', part2)
assert part2 == 45000
print('Part 2:', solve2(lines))