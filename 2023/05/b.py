import re
from collections import defaultdict
from functools import cache
E: list

def solve(example: list) -> int:
    ret_val = 0
    index = "seed"
    last = ""
    global E
    E = example
    # saved = defaultdict(lambda: [])
    init = [int(x) for x in re.findall(r"\d+", example[0])]
    starting_vals = [(init[x], init[x] + init[x + 1]) for x in range(0, len(init), 2)]
    end_vals = []
    for init in starting_vals:
        # print(init)

        # print(init)
        end_vals.append(naive(*init))
        # print(index, init)
        # return 0
    # init = list(local_mapping.values())
    # print(init)
    # print(min([x[0] for x in init]))
    # print("end_vals", end_vals)
    # return 0
    return min(end_vals)


# 2427826 low
# 3427826 low
# 1209828

def naive(x:int, y:int) -> int:
    mid = (x + y) // 2
    if mid - x > 50000000:
        return min([naive(x, mid), naive(mid, y)])
    return min([logic(x, mid), logic(mid, y)])

@cache
def logic( x:int, y:int) -> int:
    local_mapping = {}
    print((x, y))


    init = [x for x in range(x, y)]
    for i, line in enumerate(E[1:]):
        if not line:
            continue
        # print(line)
        if "map" in line:
            # last: str = re.findall(r"\w+", line)[0]
            # index: str = re.findall(r"\w+", line)[2]
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