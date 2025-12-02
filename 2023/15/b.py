from typing import List
from collections import defaultdict


def _hash(line: str) -> int:
    ret = 0
    for c in line:
        asc = ord(c)
        ret += asc
        ret *= 17
        ret %= 256
    return ret


def solve(example: List[str]) -> int:
    ret_val = 0
    hash_map = defaultdict(lambda: {})
    instructions = example[0].split(",")
    for ins in instructions:
        ret = 0
        if "=" in ins:
            label, strength = ins.split("=")
            box_i = _hash(label)
            hash_map[box_i][label] = strength
            # print(label, box_i)

        elif "-" in ins:
            label, strength = ins.split("-")
            box_i = _hash(label)
            hash_map[box_i].pop(label, None)
    for k, v in hash_map.items():
        # print(k, v)
        for i, vv in enumerate(v.values()):
            # print(k +1, i+1, vv, "=", (k+1) * (i+1) * int(vv))
            # print((k+1) * (i+1) * int(vv))
            ret_val += (k + 1) * (i + 1) * int(vv)
    return ret_val
