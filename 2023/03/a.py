import re


def solve(example: list) -> int:
    numbers_line = []
    for line in example:
        numbers_line.append([[m.group(), m.start()] for m in re.finditer(r"\d+", line)])

    ret_val = 0
    for i, numbers in enumerate(numbers_line):
        for number in numbers:
            num_value = number[0]
            num_index = number[1]
            num_str = ""
            for line in range(max(0, i - 1), min(i + 2, len(example))):  # upper bound?
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

            if num_str.replace(".", "") != num_value:
                ret_val += int(num_value)

    return ret_val
