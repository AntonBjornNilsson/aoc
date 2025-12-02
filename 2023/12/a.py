from typing import List

import sys
import copy

sys.setrecursionlimit(25000)


def _is_good(line: str, nums: list) -> bool:
    ret = [x for x in line.split(".") if x]
    return False


def solve_one_line(line: str, nums: list, index: int = 0):
    # ?###???????? 3,2,1 == 10
    # .??..??...?##. 1,1,3 == 4
    ret = 0
    # if len([x for x in line if x == "#"]) == 0:
    #     if len(nums) == 0:
    #         print("found one")
    #         return 1
    #     return 0
    if not nums:
        return 1 if "#" not in line else 0
    c = line[0]
    num, nums = nums[0], nums[1:]
    earliest_possible = len(line) - sum(nums) - len(nums) - num + 1
    for i in range(0, earliest_possible):
        if "#" in line[:i]:
            break
        i_next = i + num
        stepper = line[i:i_next]
        remaining = line[i_next + 1 :]
        edge_case: bool = line[i_next : i_next + 1] != "#"
        if i_next <= len(line):
            if "." not in stepper and edge_case:
                index += solve_one_line(remaining, nums)
    return index
    # if c == '.':
    #     # print(".", line)
    #     ret += solve_one_line(line[1:], nums)
    # elif c == '?':
    #     # print("?", line)

    #     ret += solve_one_line('.'+line[1:], nums)
    #     ret += solve_one_line('#'+line[1:], nums)
    # elif c == '#':
    #     g_len = -1
    #     if "." in line or '?' in line:
    #         g_len = max(line.find('.'),line.find('?'))
    #     else:
    #         g_len = len(line)

    #     print("found #", line, g_len, "x", nums)
    #     if nums and (nums[0] < g_len ):
    #         # print("#", line, g_len)
    #         print("from", line, "to", line[nums[0]:], "g_len", g_len)
    #         ret += solve_one_line(line[nums[0]:], nums[1:])
    #         print(ret)

    # custom_str = line.replace("?", '.')
    # if _is_good(custom_str, nums):
    #     ret += 1
    # else:
    #     solve_one_line(line[1:], nums, i)
    # print("here?")

    # return ret


def solve(example: List[str]) -> int:
    ret_val = 0
    for i, line in enumerate(example):
        char_sec, num_sec = line.split(" ")
        nums = [int(x) for x in num_sec.split(",")]
        # print(i, char_sec, nums)
        ret = solve_one_line(char_sec, nums)
        print(i, char_sec, ret, "-" * 50)
        ret_val += ret
        # if i == 2:
        #     assert ret == 1
        # if i == 0:
        #     assert ret == 1
        # if i == 1:
        #     assert ret == 4

    return ret_val


# 7169
