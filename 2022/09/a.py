#!/usr/local/env python
import math
from pathlib import Path


with (Path(__file__).parent / "input.txt").open() as text:

    lines = [line.strip() for line in text.read().split("\n") if line]


def vis(head, tail):
    for y in reversed(range(5)):
        for x in range(6):
            # if [y, x] == head and head == tail:
            #     print("same")
            if (y, x) == head:
                print("H", end="")
            elif (y, x) == tail:
                print("T", end="")
            else:
                print(".", end="")

        print()
        # print(head, tail)


def vis_tails(tails):
    print("--------------")
    for y in reversed(range(5)):
        for x in range(6):
            # if [y, x] == head and head == tail:
            #     print("same")

            if (y, x) in tails:
                print("#", end="")
            else:
                print(".", end="")

        print()
        # print(head, tail)


def move_right(pos):
    return (pos[0], pos[-1] + 1)


def move_left(pos):
    return (pos[0], pos[-1] - 1)


def move_up(pos):
    return (pos[0] + 1, pos[-1])


def move_down(pos):
    return (pos[0] - 1, pos[-1])


reverse_mapping = {
    move_down: move_up,
    move_up: move_down,
    move_left: move_right,
    move_right: move_left,
}


def step_func(head_func, steps, tails, head, tail):
    for _ in range(steps):
        head = head_func(head)
        if math.dist(head, tail) > 1.5:
            tail = reverse_mapping[head_func](head)
        if tail not in tails:
            tails.append(tail)
    return head, tail


def solve(init_list: list) -> int:
    head = (0, 0)
    tail = (0, 0)
    tail_spots = [(0, 0)]
    for line in init_list:
        steps = int(line[2:])
        if "R" in line:
            head, tail = step_func(move_right, steps, tail_spots, head, tail)
        if "L" in line:
            head, tail = step_func(move_left, steps, tail_spots, head, tail)
        if "U" in line:
            head, tail = step_func(move_up, steps, tail_spots, head, tail)
        if "D" in line:
            head, tail = step_func(move_down, steps, tail_spots, head, tail)
        # vis(head, tail)
    # vis_tails(tail_spots)
    return len(tail_spots)


# def solve2(init_list: list) -> int:


example = [
    e.strip()
    for e in """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".split(
        "\n"
    )
    if e
]


part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 13
print("Part 1:", solve(lines))

# 6036 -
# 6081 Correct
