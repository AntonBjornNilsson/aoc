#!/usr/local/env python
import math
from pathlib import Path
from typing import Callable, List, Set


with (Path(__file__).parent / "input.txt").open() as text:

    lines = [line.strip() for line in text.read().split("\n") if line]


def vis(head, tails):
    print("--------------", len(tails), tails)
    for y in reversed(range(20)):
        for x in range(20):
            to_be_written = "."
            if (y, x) == head:
                to_be_written = "H"
            for tail in range(len(tails)):

                if (y, x) == tails[tail] and (y, x) != head:
                    to_be_written = tail
                    break

            print(to_be_written, end="")

        print()
        # print(head, tail)


def vis_tails(tails):
    print("--------------")
    for y in reversed(range(20)):
        for x in range(20):
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


def step_func(
    head_func: Callable,
    ret_tails: List[Set[int]],
    head: Set[int],
    tails: List[Set[int]],
):
    temp = []
    head = head_func(head)
    if not len(tails):
        return head, []
    if head == tails[0]:
        return head, tails
    h = tails[0]
    if math.dist(head, tails[0]) > 1.5:
        # tails[0] = reverse_mapping[head_func](head)
        h, temp = step_func(
            head_func=reverse_mapping[head_func],
            ret_tails=ret_tails,
            head=tails[0],
            tails=tails[1:],
        )
        tails = [h] + temp

    if len(tails) == 1 and tails[-1] not in ret_tails:
        ret_tails.append(tails[-1])

    return head, tails


def solve2(init_list: list) -> int:
    head = (0, 0)
    tails = [(0, 0)] * 10
    print(tails)
    tail_spots = [(0, 0)]
    for line in init_list[:2]:
        steps = int(line[2:])
        if "R" in line:
            for _ in range(steps):
                head, tails = step_func(
                    head_func=move_right,
                    ret_tails=tail_spots,
                    head=head,
                    tails=tails,
                )
                vis(head, tails)

        if "L" in line:
            for _ in range(steps):
                head, tails = step_func(
                    head_func=move_left,
                    steps=steps,
                    ret_tails=tail_spots,
                    head=head,
                    tails=tails,
                )
        if "U" in line:
            for _ in range(steps):
                head, tails = step_func(
                    head_func=move_up,
                    steps=steps,
                    ret_tails=tail_spots,
                    head=head,
                    tails=tails,
                )
        if "D" in line:
            for _ in range(steps):
                head, tails = step_func(
                    head_func=move_down,
                    steps=steps,
                    ret_tails=tail_spots,
                    head=head,
                    tails=tails,
                )
        print(tails)

        # vis(head, tails)
    vis_tails(tail_spots)
    return len(tail_spots)


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

example2 = [
    e.strip()
    for e in """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".split(
        "\n"
    )
    if e
]


part2 = solve2(example)
print("Example part 2:", part2)
# part22 = solve2(example2)
print("Example part 2:", part22)
assert part2 == 1
assert part22 == 36
print("Part 2:", solve2(lines))
