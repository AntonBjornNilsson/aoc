#!/usr/local/env python
import json
from pathlib import Path


with (Path(__file__).parent / "input.txt").open() as text:

    lines = [line.strip() for line in text.read().split("\n") if line]


def reqr(left, right):
    assert len(left) == len(right)
    if isinstance(left, list) and isinstance(right, list):
        return reqr(left[0])


def solve(init_list) -> int:
    for i in range(0, len(init_list), 2):
        left, right = json.loads(init_list[i]), json.loads(init_list[i + 1])
        print(left)
        print(right)
        print("-----------")
        reqr(left, right)
    return 0


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
