from typing import List


def solve(example: List[str]) -> int:
    ret_val = 0
    instructions = example[0].split(",")
    for ins in instructions:
        ret = 0
        for c in ins:
            asc = ord(c)
            ret += asc
            ret *= 17
            ret %= 256
        ret_val += ret
        assert ret > -1 and ret < 256
    return ret_val
