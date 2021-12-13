#!/usr/local/env python
from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as text:
    lines = [ line.strip() for line in text.read().split("\n") if line]

def fold_x(coords: list, x_line: int) -> list:
    new_coords = []
    right = x_line * 2
    for index in range(len(coords)):
        cached = coords[index]
        new_x = abs(cached[0] - right)
        flipped = [new_x, cached[1]]
        if flipped in new_coords:
            continue
        if cached[0] > x_line:
            new_coords.append(flipped)
        elif cached[0] == x_line:
            continue
        else:
            new_coords.append(cached)
    return new_coords

def fold_y(coords: list, y_line: int) -> list:
    new_coords = []
    down = y_line * 2
    for index in range(len(coords)):
        cached = coords[index]
        new_y = abs(cached[1] - down)
        flipped = [cached[0], new_y]
        if flipped in new_coords:
            continue
        if cached[1] > y_line:
            new_coords.append(flipped)
        elif cached[1] == y_line:
            continue
        else:
            new_coords.append(cached)
    return new_coords

def solve(init_list: list) -> int:
    coords = [[int(i) for i in x.split(",")] for x in init_list if "fold" not in x]
    folds = [[f for f in x.replace("fold along ","").split("=")] for x in init_list if "fold" in x]
    # folds = [folds[0]]
    print(folds)
    # print_paper(coords)
    for fold in folds:
        if fold[0] == "x":
            coords = fold_x(coords, int(fold[1]))
        elif fold[0] == "y":
            coords = fold_y(coords, int(fold[1]))
        else:
            print("error")
            exit(0)
        # print_paper(coords)
    print_paper(coords)
    return len(coords)


# def solve2(init_list: list) -> int:

def print_paper(coords: list):
    right = max([c[0] for c in coords])
    down = max([c[1] for c in coords])
    print("-------------------------------------")
    print(coords, len(coords))
    for y in range(down + 1):
        for x in range(right + 1):
            if [x, y] in coords:
                print("#", end="")
            else:
                print(".", end = "")
        print()
    print("-------------------------------------")


example = [ e.strip() for e in """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".split("\n") if e ]


part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 17
print("Part 1:", solve(lines))
# 685 < x < 778