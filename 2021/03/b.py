#!/usr/local/env python
import math
from pathlib import Path
import operator

each_line_is_bool = False
with (Path(__file__).parent / "input.txt").open() as text:
    lines = [line.strip() for line in text.readlines() if line]


def solve(init_list: list) -> int:
    length = len(init_list[0])
    gamma_delta = []
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
    inverse_bit = "".join(["1" if i == "0" else "0" for i in bit])
    gamma = int(bit, 2)
    epsilon = int(inverse_bit, 2)
    return gamma * epsilon


def inner_solve2(
    init_list: list,
    operator,
    index: int = 0,
) -> int:
    length = len(init_list[0])
    for i in range(index, length):
        one_list = []
        zero_list = []
        for bin in init_list:
            zeros = 0
            ones = 0
            for bin in init_list:
                if bin[i] == "1":
                    ones += 1
                    one_list.append(bin)
                if bin[i] == "0":
                    zeros += 1
                    zero_list.append(bin)

            if operator(len(one_list), len(zero_list)):
                if len(one_list) > 1:
                    return inner_solve2(one_list, operator, index + 1)
                else:
                    return one_list[0]
            else:
                if len(zero_list) > 1:
                    return inner_solve2(zero_list, operator, index + 1)
                else:
                    return zero_list[0]


def solve2(init_list: list) -> int:
    o2 = int(inner_solve2(init_list, operator.ge), 2)
    co2 = int(inner_solve2(init_list, operator.lt), 2)
    return o2 * co2


example = [
    e
    for e in """00100
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
""".split(
        "\n"
    )
    if e
]
if each_line_is_bool:
    example = [int(e) for e in example if e]

part1 = solve(example)
print("Unit A", part1)
assert part1 == 198
print("Part 1:", solve(lines))

part2 = solve2(example)
print("Unit B", part2)
assert part2 == 230
print("Part 2:", solve2(lines))
