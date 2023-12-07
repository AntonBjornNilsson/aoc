import re
from collections import defaultdict


def solve(example: list) -> int:
    ret_val = 0
    index = "seed"
    last = ""
    # saved = defaultdict(lambda: [])
    init = [int(x) for x in re.findall(r"\d+", example[0])]
    local_mapping = {}

    for i, line in enumerate(example[1:]):
        if not line:
            continue
        # print(line)
        if "map" in line:
            last: str = re.findall(r"\w+", line)[0]
            index: str = re.findall(r"\w+", line)[2]
            init = [
                local_mapping[value] if value in local_mapping else value
                for value in init
            ]
            local_mapping = {}

            continue
        # saved[index].append([ int(x) for x in re.findall(r'\d+', line)])
        dst_start, src_start, _len = [int(x) for x in re.findall(r"\d+", line)]

        for x in init:
            if x >= src_start and x < src_start + _len:
                local_mapping[x] = dst_start + (x - src_start)

        # for dst_val, src_val in zip(range(dst_start, dst_start + _len), range(src_start, src_start + _len)):

        # print(index, init)

    init = [local_mapping[value] if value in local_mapping else value for value in init]
    # print(index, init)

    return min(init)
