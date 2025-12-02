from typing import List
import numpy as np
from .a import eval_load


def tramsform(line: list, index: int = 0) -> int:

    try:
        stopper = line.index("#")
    except ValueError:
        stopper = len(line)
    # count = [max_val - index - x for x in range(line[:stopper].count("O"))]
    count = line[:stopper].count("O")
    # print(stopper, count, line[:stopper])
    if stopper != len(line):  # "O" in line[stopper+1:]
        # print("do, recr", stopper, line)
        return (
            ["O" if x < count else "." for x in range(stopper)]
            + ["#"]
            + (
                tramsform(line[stopper + 1 :], index=stopper + index + 1)
                if "O" in line[stopper + 1 :]
                else line[stopper + 1 :]
            )
        )
    return ["O" if x < count else "." for x in range(stopper)]


def trams_matrix(matrix: list) -> None:
    ret_val = 0
    for i, line in enumerate(matrix):
        matrix[i] = tramsform(matrix[i])
    # return ret_val


def eval_load(max_val: int, line: list, index: int = 0) -> int:

    # try:
    #     stopper = line.index("#")
    # except ValueError:
    #     stopper = len(line)
    # count = [max_val - index - x for x in range(line[:stopper].count("O"))]
    # print(count)
    # if stopper != len(line) and "O" in line[stopper+1:]:
    #     return sum(count) + eval_load(max_val, line[stopper+1:], index=stopper + index +1)
    return sum([max_val - x for x in range(max_val) if line[x] == "O"])


def eval_matrix(matrix: list) -> int:
    ret_val = 0
    for line in matrix:
        ret_val += eval_load(len(line), line)
        # print(line, "is worth", eval_load(len(line), line), "len", len(line))
    # grid = np.transpose(matrix).tolist()
    # print("EVAL", ret_val)
    # for x in matrix:
    #     print(x)
    # print("EVAL")
    return ret_val


def solve(example: List[str]) -> int:
    ret_val = 0
    last_val = 0
    # col to row
    grid = [list(row) for row in example]
    # temp = np.array([list(row) for row in example])
    # grid = np.transpose(temp).tolist()
    # nice_print(grid)
    # temp = np.array(grid)
    # grid = np.rot90(temp, k=3).tolist()
    # print()
    # nice_print(grid)
    temp = np.array(grid)
    grid = np.transpose(grid).tolist()
    # grid = np.rot90(temp, k=3).tolist()
    ret_list = []
    for cycle in range(1, 1001):
        # to_north
        # print(grid,type(grid))
        # for x in grid:
        #     print(x, type(x))
        for ord in ["north", "west", "south", "east"]:
            # print("flipping to", ord)
            # nice_print(grid)
            # print()
            temp = np.array(grid)
            # grid = np.transpose(temp).tolist()
            trams_matrix(grid)
            temp = np.array(grid)
            # temp = np.transpose(temp)
            grid = np.rot90(temp, k=1).tolist()
            # nice_print(grid)

        # trams_matrix(grid)
        # trams_matrix(grid)

        print("after cycle:", cycle, eval_matrix(grid))
        # temp = np.array(grid)
        # temp = np.transpose(temp)
        # grid = np.rot90(temp, k=1).tolist()
        # nice_print(grid)
        ret_val = eval_matrix(grid)

        # if cycle > 3:
        #     exit(0)
        ret_list.append(ret_val)

        # if last_val == ret_val:
        #     print("found in cycle", cycle)
        #     break
        # last_val = ret_val
    print(ret_list)
    print([ret_list[x] for x in range(len(ret_list)) if x % 10 == 0])

    return ret_val


def nice_print(grid: list) -> None:
    temp = np.array([list(row) for row in grid])
    grid = np.transpose(temp).tolist()
    for x in grid:
        print(x)


# 96447, lucky endpoint. 10**3 was the same as 10**9
