from typing import List


def is_bad_value(value: int) -> bool:
    str_val = str(value)

    for times in range(2, len(str_val) + 1):
        if len(str_val) % times != 0:
            continue
        inverse_times = len(str_val) // times
        composites = [
            str_val[x : x + inverse_times]
            for x in range(0, times * inverse_times, inverse_times)
        ]
        if len(set(composites)) == 1:
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

