#!/usr/local/env python
from pathlib import Path

each_line_is_bool = False
with (Path(__file__).parent / "input.txt").open() as text:

    lines = [line.strip() for line in text.read().split("\n") if line]


def check_winner(board: list, called_numbers: list) -> bool:
    if len(board) != 5:
        print(board, called_numbers)
    for y in range(5):
        if all(x in called_numbers for x in board[y]):
            return True
        for x in range(5):
            if all(f in called_numbers for f in [e[x] for e in board]):
                return True
    return False


def calc_score(board: list, called_numbers: list) -> int:
    score = 0
    for y in range(5):
        for x in range(5):
            number = board[y][x]
            if number not in called_numbers:
                score += int(number)
    return score


def solve(init_list: list) -> int:
    instructions = init_list[0].split(",")
    called_numbers = []
    boards = [
        [x.replace("  ", " ").split(" ") for x in init_list[i : i + 5] if x]
        for i in range(1, len(init_list[1:]), 5)
    ]
    for i in instructions:
        called_numbers.append(i)
        for board in boards:
            if check_winner(board, called_numbers):
                return int(i) * calc_score(board, called_numbers)


def solve2(init_list: list) -> int:
    instructions = init_list[0].split(",")
    called_numbers = []
    boards = [
        [x.replace("  ", " ").split(" ") for x in init_list[i : i + 5] if x]
        for i in range(1, len(init_list[1:]), 5)
    ]
    for i in instructions:
        called_numbers.append(i)
        for board in boards:
            if check_winner(board, called_numbers):
                if len(boards) == 1:
                    return int(i) * calc_score(board, called_numbers)
                boards.remove(board)


example = [
    e.strip()
    for e in """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".split(
        "\n"
    )
    if e
]
if each_line_is_bool:
    example = [int(e) for e in example if e]

part1 = solve(example)
print("Example part 1", part1)
assert part1 == 4512
print("Part 1:", solve(lines))

part2 = solve2(example)
print(part2)
assert part2 == 1924
print("Part 2:", solve2(lines))
