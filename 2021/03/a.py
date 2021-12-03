#!/usr/local/env python
import math
from pathlib import Path

each_line_is_bool = False
with (Path(__file__).parent / "input.txt").open() as text:
    lines = [ line.strip() for line in text.readlines() if line]


def solve(init_list: list) -> int:
    length = len(init_list[0])
    gamma_delta = []
    gamma = ""
    epsilon = ""
    for i in range(length):
        zeros = 0
        ones = 0
        for bin in init_list:
            if bin[i] == "1":
                ones += 1
            if bin[i] == "0":
                zeros += 1

        if zeros >= ones:
            gamma_delta.append(1)
        else:
            gamma_delta.append(0)
        bit = "".join([str(x) for x in gamma_delta])
    inverse_bit = ''.join(['1' if i == '0' else '0'
                     for i in bit])
    gamma = int(bit,2)
    epsilon = int(inverse_bit,2)
    return gamma * epsilon



# def solve2(init_list: list) -> int:



example = [e for e in """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".split("\n") if e]
if each_line_is_bool:
    example = [ int(e) for e in example if e ]
part1 = solve(example)
print("Unit A", part1)
assert part1 == 198
print("Part 1:", solve(lines))
