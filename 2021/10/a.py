#!/usr/local/env python
from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as text:
    lines = [line.strip() for line in text.read().split("\n") if line]

look_up = {"(": ")", "[": "]", "{": "}", "<": ">"}

value_look_up = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
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
    return None


def is_valid(line: str) -> int:
    length = len(line)

    ret = req_is_valid(line)
    if ret:
        return ret
    return 0


def solve(init_list: list) -> int:
    count = 0
    for line in init_list:
        count += is_valid(line)
    return count


# def solve2(init_list: list) -> int:


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

assert is_valid(test3) == 1197
assert is_valid(test5) == 3
assert is_valid(test6) == 57
assert is_valid(test8) == 3
assert is_valid(test9) == 25137

part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 26397
print("Part 1:", solve(lines))
