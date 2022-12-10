#!/usr/local/env python
from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as text:

    lines = [ line.strip() for line in text.read().split("\n") if line]


def solve(init_list: list) -> int:
    X = 1
    instruct_index = 0
    do_exec = True
    signals = []
    for cycle in range(1, 221):
        if cycle % 20 == 0 and (cycle - 20) % 40 == 0:
            sig_str = cycle * X
            signals.append(sig_str)
        line = init_list[instruct_index]
        if line == "noop":
            instruct_index += 1
        else:
            if do_exec:
                pass
            else:
                new_val = int(line[5:])
                X += new_val
                instruct_index += 1
            do_exec = not do_exec
    return sum(signals)


def solve2(init_list: list) -> int:
    X = 1
    instruct_index = 0
    do_exec = True
    signals = []
    pixels = [["0" for _ in range(40)] for _ in range(6)]
    for cycle in range(0, 240):
        row = cycle // 40
        col = cycle % 40
        # if row == 0:
        #     print(row, col)
        #     print(X, col, [X, X+1, X-1], col + 1 in [X, X+1, X-1])
        if col in [X, X+1, X-1]:
            pixels[row][col] = "#"
        else:
            pixels[row][col] = "."

        line = init_list[instruct_index]
        if line == "noop":
            instruct_index += 1
        else:
            if do_exec:
                pass
            else:
                new_val = int(line[5:])
                X += new_val
                instruct_index += 1
            do_exec = not do_exec
    for x in pixels:
        print("".join(x))
    return sum(signals)



example = [ e.strip() for e in """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".split("\n") if e ]

part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 13140
print("Part 1:", solve(lines))

# 15260 Correct

part2 = solve2(example)
print('Example part 2:', part2)
# assert part2 == -1
print('Part 2:', solve2(lines))

###...##..#..#.####..##..#....#..#..##..
#..#.#..#.#..#.#....#..#.#....#..#.#..#.
#..#.#....####.###..#....#....#..#.#....
###..#.##.#..#.#....#.##.#....#..#.#.##.
#....#..#.#..#.#....#..#.#....#..#.#..#.
#.....###.#..#.#.....###.####..##...###.
