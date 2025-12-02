from typing import List
import numpy as np


def _eval_grid(grid: list) -> int:
    for i in range(len(grid) - 1):
        do_ret = True
        if grid[i] != grid[i + 1]:
            continue
        # print(i, "is equal to", i + 1)
        # print(grid[i], grid[i+1])
        try:
            # print(list(range(0, i+1)))
            for x in range(0, i + 1):
                # print("checking", i-x, i+1+x)
                if grid[i - x] == grid[i + 1 + x]:
                    continue
                # print("escaped", grid[i-x], i-x, "is not same as")
                # print(grid[i+1+x], i+1+x)
                do_ret = False
                break
            # print(print("escaped in break, last known x was",x ))
            if do_ret:
                # print("return", i +1 )
                return i + 1
        except IndexError:
            # print("escaped in try, last known x was",x )
            return i + 1
    return 0


def solve(example: List[str]) -> int:
    ret_val = 0
    split_examples = [[]]
    index = 0
    for i, line in enumerate(example):
        if line == "":
            split_examples.append([])
            continue
        split_examples[-1].append(line)
    # for ex in split_examples:
    #     for l in ex:
    #         print(l)
    #     print("---")

    for grid in split_examples:
        # find up/down
        # for x in grid:
        #     print(x)
        # print()
        ret = _eval_grid(grid)
        ret_val += ret * 100

        # find left/right
        if ret == 0:
            temp = np.array([list(row) for row in grid])
            grid = np.transpose(temp).tolist()
            # for x in grid:
            #     print("".join(x))
            # print()
            # grid = np.fliplr(temp).tolist()
            ret = _eval_grid(grid)
            ret_val += ret
        # print(ret_val, "r")

    return ret_val
