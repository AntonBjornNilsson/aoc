#!/usr/local/env python
from pathlib import Path
import math

with (Path(__file__).parent / "input.txt").open() as text:
    lines = [line.strip() for line in text.read().split("\n") if line]

look_up = {"(": ")", "[": "]", "{": "}", "<": ">"}

value_look_up = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def req_is_valid(line: str, expected: str = "", depth: int = 0):
    stack = []
    for char in line:
        if char in look_up.keys():
            stack.append(char)

        elif char in look_up.values():
            matching = stack.pop()
            if look_up[matching] == char:
                continue
            return value_look_up[char]
    return stack


def is_valid(line: str) -> int:
    length = len(line)
    count = 0
    ret = req_is_valid(line)
    if isinstance(ret, list):
        for char in ret[::-1]:
            count *= 5
            count += value_look_up[look_up[char]]
        print("cost of", line, "was", count)
        return count
    return 0


def solve(init_list: list) -> int:
    _all = []
    for line in init_list:
        score = is_valid(line)
        if score:
            _all.append(score)
    _all.sort()
    mid = math.floor(len(_all) / 2)
    return _all[mid]


example = [
    e.strip()
    for e in """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".split(
        "\n"
    )
    if e
]


test1 = "[({(<(())[]>[[{[]{<()<>>"
test2 = "[(()[<>])]({[<{<<[]>>("
test3 = "{([(<{}[<>[]}>{[]{[(<()>"
test4 = "(((({<>}<{<{<>}{[]{[]{}"
test5 = "[[<[([]))<([[{}[[()]]]"
test6 = "[{[{({}]{}}([{[{{{}}([]"
test7 = "{<[[]]>}<{[{[{[]{()[[[]"
test8 = "[<(<(<(<{}))><([]([]()"
test9 = "<{([([[(<>()){}]>(<<{{"
test10 = "<{([{{}}[<[[[<>{}]]]>[]]"

assert is_valid(test1) == 288957
assert is_valid(test2) == 5566
assert is_valid(test4) == 1480781
assert is_valid(test7) == 995444
assert is_valid(test10) == 294


part2 = solve(example)
print("Example part 2:", part2)
assert part2 == 288957
print("Part 2:", solve(lines))
