#!/usr/local/env python
from pathlib import Path


with (Path(__file__).parent / "input.txt").open() as text:
    lines = text.read()


def solve(init_str: list) -> int:
    tot = 0
    for i in range(len(init_str)):
        test = init_str[i : i + 14]
        if len(list(set(test))) == len(test):
            return i + 14
    return tot


e = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
part1 = solve(e)
print("Example part 1:", part1)
assert part1 == 19
e = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
part1 = solve(e)
print("Example part 1:", part1)
assert part1 == 23
e = """nppdvjthqldpwncqszvftbrmjlhg"""
part1 = solve(e)
print("Example part 1:", part1)
assert part1 == 23
e = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
part1 = solve(e)
print("Example part 1:", part1)
assert part1 == 29
e = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""
part1 = solve(e)
print("Example part 1:", part1)
assert part1 == 26

# 2315 correct


print("Part 1:", solve(lines))
