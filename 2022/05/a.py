#!/usr/local/env python
from pathlib import Path
from typing import List
import re

with (Path(__file__).parent / "input.txt").open() as text:

    lines = [line for line in text.read().split("\n")]


def parse(_list: List[str]):
    for i, line in enumerate(_list):
        if line == "":
            break
    max_elem = int(_list[i - 1][-1])
    ret_list = [[] for _ in range(max_elem)]
    for i, line in enumerate(_list):
        for index, char_i in enumerate(range(1, len(line), 4)):
            if line[char_i] != " ":
                if not line[char_i].isdigit():
                    ret_list[index].append(line[char_i])
        if line == "":
            break
    [x.reverse() for x in ret_list]
    i_list = []
    for instruct in range(i + 1, len(_list)):
        count, f, t = re.findall(r"\d+", _list[instruct])
        i_list.append((int(count), int(f) - 1, int(t) - 1))
    return ret_list, i_list


def solve(init_list: list) -> int:
    _list, instructions = parse(init_list)
    for count, f, t in instructions:
        for _ in range(count):
            elem = _list[f].pop()
            _list[t].append(elem)
    ret = "".join([x[-1] for x in _list if x])
    return ret


# def solve2(init_list: list) -> int:


example = [
    e
    for e in """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split(
        "\n"
    )
]

part1 = solve(example)
print("Example part 1:", part1)
assert part1 == "CMZ"
print("Part 1:", solve(lines))

# JCMHLVGMG correct
