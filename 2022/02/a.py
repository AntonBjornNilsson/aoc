#!/usr/local/env python
from pathlib import Path


with (Path(__file__).parent / "input.txt").open() as text:
    lines = [line for line in text.read().split("\n")]


class op:
    rock = "A"
    paper = "B"
    scissor = "C"


class you:
    rock = "X"
    paper = "Y"
    scissor = "Z"


you_gain = {
    you.rock: 1,
    you.paper: 2,
    you.scissor: 3,
}
win_loss = {
    op.rock: {
        you.rock: 3,
        you.paper: 6,
        you.scissor: 0,
    },
    op.paper: {
        you.rock: 0,
        you.paper: 3,
        you.scissor: 6,
    },
    op.scissor: {
        you.rock: 6,
        you.paper: 0,
        you.scissor: 3,
    },
}


def solve(init_list: list) -> int:
    tot = 0
    print("here")
    for line in init_list:
        ops, yous = line.split(" ")
        tot += win_loss[ops][yous] + you_gain[yous]
    return tot


# def solve2(init_list: list) -> int:


example = [
    e.strip()
    for e in """A Y
B X
C Z
""".split(
        "\n"
    )
    if e
]


part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 15
print("Part 1:", solve(lines))
