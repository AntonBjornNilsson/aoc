from typing import List
import numpy as np


def count_different_chars(str1, str2):
    # thanks chatgpt for this one
    # Ensure the strings are of the same length
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")

    # Count the differing characters
    count = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            count += 1

    return count


def _eval_grid(grid: list) -> int:
    for i in range(len(grid)):
        do_ret = True
        for u in range(i + 1, len(grid)):
            if count_different_chars(grid[i], grid[u]) != 1:
                continue
            # if (u+1)-(i +1) % 2 == 1:
            #     continue
            print(i, "has one diff to", u)
            print(grid[i], grid[u])
            try:
                print(list(range(1, u - i)))
                if list(range(1, u - i)) == []:
                    print("ret same", i, u)
                    return i + 1
                for x in range(1, u - i):
                    print("checking", i + x, u - x)
                    if i + x == u - x:
                        do_ret = True
                        break
                    # if i-x < 0 or i + 1+ x >len(grid[0]):
                    # break
                    if grid[i + x] == grid[u - x]:
                        continue
                    print("escaped", grid[i + x], u - x, "is not same as")
                    # print(grid[i+1+x], i+1+x)
                    do_ret = False
                    break
                # print("escaped in break, last known x was",x )
                if do_ret:
                    # print("return", (i+1 + u+1) // 2 )
                    return (i + 1 + u + 1) // 2
            except IndexError:
                # print("escaped in try, last known x was",x )
                return (i + 1 + u + 1) // 2
    # print("REVERTING")
    # from .a import _eval_grid as old
    # return old(grid)
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

    for i, grid in enumerate(split_examples):
        # find up/down
        print("-" * 50)
        for u, x in enumerate(grid):
            print(u, x)

        from .a import _eval_grid as old

        x = old(grid)
        # if ret == 0:
        ret = _eval_grid(grid)
        if x != 0:
            assert x != ret, f"{x} is the same as {ret}"
        # else:
        #     print("FOUND AN OLD SOLUTION", ret)
        ret_val += ret * 100

        # find left/right
        if ret == 0:
            temp = np.array([list(row) for row in grid])
            grid = np.transpose(temp).tolist()
            # for x in grid:
            #     print("".join(x))
            # print()
            # grid = np.fliplr(temp).tolist()
            from .a import _eval_grid as old

            x = old(grid)
            ret = _eval_grid(grid)
            if x != 0:
                assert x != ret, f"{x} is the same as {ret}"
            ret_val += ret
        print("grid_nbr", i, "ret", ret, "total", ret_val)
        # if i == 0:
        #     assert ret == 3
        # if i == 1:
        #     assert ret == 1
        # if i == 2:
        #     assert ret == 2
        # if i == 3:
        #     assert ret == 6, ret
        # if i == 4:
        #     assert ret == 6, ret

    return ret_val


# 33560 low
# 43100 high
# 40000 low
# 41182 wrong
# 41566
