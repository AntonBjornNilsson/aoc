#!/usr/local/env python
import json
from pathlib import Path


with (Path(__file__).parent / "input.txt").open() as text:

    lines = [line.strip() for line in text.read().split("\n") if line]


def recr(left, right, badness, i):
    for l_index in range(len(left)):
        # if l_index > len(left):
        #     print("ran out")
        #     findings.append(i)
        #     break
        # if len(left) == 0:
        #     print("parsing", left, right, i)
        #     findings.append(i)
        #     break
        # if len(right) == 0:
        #     break

        if l_index >= len(right):
            print("length", left, right, i)
            badness.append(i)
            break
        l, r = left[l_index], right[l_index]

        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                break
            if r < l:
                print("ints", l, r, i)
                badness.append(i)
                break

        elif isinstance(l, list) and isinstance(r, list):
            recr(l, r, badness, i)
        else:
            if isinstance(l, int) and isinstance(r, list):
                l = [l]
            if isinstance(r, int) and isinstance(l, list):
                r = [r]
            recr(l, r, badness, i)


def solve(init_list: list) -> int:
    pairings = []
    for i in range(0, len(init_list), 2):
        f, s = json.loads(init_list[i]), json.loads(init_list[i + 1])
        pairings.append((f, s))

    badness = []
    for i, (left, right) in enumerate(pairings):
        # print(left, right)
        recr(left, right, badness, i + 1)

    goodness = [x for x in range(1, len(pairings)) if x not in badness]
    print(badness, goodness)
    return goodness


# def solve2(init_list: list) -> int:


example = [
    e.strip()
    for e in """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".split(
        "\n"
    )
    if e
]


part1 = solve(example)
print("Example part 1:", part1)
assert part1 == [1, 2, 4, 6]
assert sum(part1) == 13
print("Part 1:", sum(solve(lines)))

# 20175 +
# 626 -
