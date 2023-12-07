import re
from collections import defaultdict
import math


def solve(example: list) -> int:
    numbers_line = []
    for line in example:
        numbers_line.append([[m.group(), m.start()] for m in re.finditer(r"\d+", line)])

    gears = defaultdict(lambda: [])
    ret_val = 0
    for i, numbers in enumerate(numbers_line):
        for number in numbers:
            num_value = number[0]
            num_index = number[1]
            num_str = ""
            gear_coord = None
            for line in range(max(0, i - 1), min(i + 2, len(example))):
                for col in range(
                    max(0, num_index - 1),
                    min(num_index + len(num_value) + 1, len(example[i])),
                ):
                    char = example[line][col]
                    if char == "*":
                        gear_coord = (line, col)
                _num_str = "".join(
                    [
                        example[line][col]
                        for col in range(
                            max(0, num_index - 1),
                            min(num_index + len(num_value) + 1, len(example[i])),
                        )
                    ]
                )
                num_str += _num_str
            if gear_coord is not None:
                gears[gear_coord].append(int(num_value))

    for gear_list in gears.values():
        if len(gear_list) > 1:
            ret_val += math.prod(gear_list)

    return ret_val
