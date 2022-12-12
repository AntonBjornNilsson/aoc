#!/usr/local/env python
from pathlib import Path


with (Path(__file__).parent / "input.txt").open() as text:
    lines = [line for line in text.read().split("\n")]


class op:
    rock = "A"
    paper = "B"
    scissor = "C"


class you:
    loss = "X"
    draw = "Y"
    win = "Z"


you_gain = {
    you.draw: 3,
    you.loss: 0,
    you.win: 6,
}
# 1 rock
# 2 paper
# 3 scissor
win_loss = {
    op.rock: {
        you.draw: 1,
        you.loss: 3,
        you.win: 2,
    },
    op.paper: {
        you.draw: 2,
        you.loss: 1,
        you.win: 3,
    },
    op.scissor: {
        you.draw: 3,
        you.loss: 2,
        you.win: 1,
    },
}


def solve2(init_list: list) -> int:
    tot = 0
    print("here")
    for line in init_list:
        ops, yous = line.split(" ")
        tot += win_loss[ops][yous] + you_gain[yous]

        print(ops, yous)
        print(win_loss[ops][yous], you_gain[yous])
        print(tot)
    return tot


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

part2 = solve2(example)
print("Example part 2:", part2)
assert part2 == 12
print("Part 2:", solve2(lines))
# 16959
