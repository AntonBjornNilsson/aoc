#!/usr/local/env python
from pathlib import Path

each_line_is_bool = False
with (Path(__file__).parent / "input.txt").open() as text:
    try:
        lines = [int(line) for line in text.read().split("\n") if line]
        each_line_is_bool = True
    except ValueError:
        lines = [line.strip() for line in text.read().split("\n") if line]


def solve(init_list: list) -> int:
    return 0


# def solve2(init_list: list) -> int:


example = [
    e.strip()
    for e in """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
""".split(
        "\n"
    )
    if e
]
if each_line_is_bool:
    example = [int(e) for e in example if e]

part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 1651
print("Part 1:", solve(lines))
