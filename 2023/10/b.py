from time import sleep
from typing import List
import networkx as nx
import sys
import copy
sys.setrecursionlimit(25000)
from matplotlib.path import Path

s = ['S']
from_west = ['-', '7', 'J'] + s
from_east = ['-', 'L', 'F'] + s
from_north = ['|', 'J', 'L'] + s
from_south = ['|', '7', 'F'] + s

def stepper(example:list, node: tuple, step: tuple) -> None:

    row, col = node
    print(node)
    visited = []
    ret = 1
    while example[node[0]][node[1]] != "S":

        char = example[node[0]][node[1]]
        print(char, node, step)
        # sleep(0.1)
        visited.append([node[0],node[1]])
        if char == "|":
            if step == [1, 0]:
                node[0] += 1
            elif step == [-1, 0]:
                node[0] -= 1
        elif char == "-":
            if step == [0, 1]:
                node[1] += 1
            elif step == [0, -1]:
                node[1] -= 1
        elif char == "7":
            if step == [0, 1]:
                node[0] += 1
                step = [1, 0]
            elif step == [-1, 0]:
                node[1] -= 1
                step = [0, -1]
        elif char == "J":
            if step == [0, 1]:
                node[0] -= 1
                step = [-1, 0]
            elif step == [1, 0]:
                node[1] -= 1
                step = [0, -1]
        elif char == "L":
            if step == [0, -1]:
                node[0] -= 1
                step = [-1, 0]
            elif step == [1, 0]:
                node[1] += 1
                step = [0, 1]
        elif char == "F":
            if step == [0, -1]:
                node[0] += 1
                step = [1, 0]
            elif step == [-1, 0]:
                node[1] += 1
                step = [0, 1]
        else:
            if char == ".":
                print("found nothing")
                break
            print("ERROR", char, visited, step)
            break
        ret += 1
    # if example[row][col] == "S":
    #     print("Found s in", node)
    #     print("east", example[row][col+1])
    #     print("south", example[row+1][col])
    #     print("west", example[row][col-1])
    #     print("north", example[row-1][col])
    return ret, visited

def solve(example: List[str]) -> int:
    start = (0,0)
    for x, line in enumerate(example):
        # print(x, line)
        for y,col in enumerate(line):
            if col == "S":
                start = (x, y)

    # ret_w = stepper(example, [start[0], start[1]-1], [0, -1])
    # ret_n = stepper(example, [start[0]-1, start[1]], [-1, 0])
    ret_w = 1
    ret_n = 1
    ret_e = 1
    # ret_e = stepper(example, [start[0], start[1] + 1], [0, 1])
    ret_s, visited = stepper(example, [start[0] +1, start[1]], [1, 0])
    print(visited)
    for y, row in enumerate(example):
        for x, col in enumerate(row):
            if [y,x] in visited:
                print("X", end="")
            else:
                print(col, end="")
        print()

    ret = 0
    print(ret_w, ret_n, ret_e, ret_s, max(ret_w, ret_n, ret_e, ret_s))

    # Couldn't figure this out, had to take help from reddit
    p = Path(visited)
    for y, row in enumerate(example):
        for x, col in enumerate(example[y]):
            if [x, y] in visited:
                continue
            if p.contains_point((x, y)):
                ret += 1

    print(ret)

    return ret -1

# 418 high
# 417, off by one