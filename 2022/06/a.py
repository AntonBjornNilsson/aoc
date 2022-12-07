#!/usr/local/env python
from pathlib import Path


with (Path(__file__).parent / "input.txt").open() as text:
    lines = text.read()




def solve(init_str: list) -> int:
    tot = 0
    for i in range(len(init_str)):
        test = init_str[i:i+4]
        if len(list(set(test))) == len(test):
            return i+4
    return tot


# def solve2(init_list: list) -> int:



e = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
part1 = solve(e)
print("Example part 1:", part1)
assert part1 == 7
e = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
part1 = solve(e)
print("Example part 1:", part1)
assert part1 == 5
e = """nppdvjthqldpwncqszvftbrmjlhg"""
part1 = solve(e)
print("Example part 1:", part1)
assert part1 == 6
e = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
part1 = solve(e)
print("Example part 1:", part1)
assert part1 == 10
e = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""
part1 = solve(e)
print("Example part 1:", part1)
assert part1 == 11

# 1538 correct

print("Part 1:", solve(lines))
