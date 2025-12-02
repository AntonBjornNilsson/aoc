from typing import List


def is_bad_value(value: int) -> bool:
    str_val = str(value)
    if len(str_val) % 2 == 1:
        return False
    f, l = str_val[: len(str_val) // 2], str_val[len(str_val) // 2 :]
    if f == l:
        return True
    return False


def solve(example: str) -> int:
    ret_val = []
    example = example.replace("\n", "")
    sets = example.split(",")
    for s in sets:
        start, end = s.split("-")
        for value in range(int(start), int(end) + 1):
            if is_bad_value(value):
                ret_val.append(value)
    return sum(ret_val)
