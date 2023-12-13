import re
from collections import defaultdict


def solve(example: list) -> int:
    ret_val = 0
    index = "seed"
    last = ""
    # saved = defaultdict(lambda: [])
    init = [int(x) for x in re.findall(r"\d+", example[0])]
    init = [(init[x], init[x] + init[x + 1]) for x in range(0, len(init), 2)]
    local_mapping = {}
    print(init)
    print(len(init))

    for i, line in enumerate(example[3:]):
        # print(i)
        if not line:
            continue
        # print(line)
        if "map" in line:
            last = re.findall(r"\w+", line)[0]
            index = re.findall(r"\w+", line)[2]
            for x in init:
                if x not in local_mapping:
                    local_mapping[x] = x
            print(last, local_mapping)
            init = list(local_mapping.values())
            local_mapping = {}

            continue
        # saved[index].append([ int(x) for x in re.findall(r'\d+', line)])
        dst_start, src_start, _len = [int(x) for x in re.findall(r"\d+", line)]
        src_range_start, src_range_end = src_start, src_start + _len  # exclusive range
        dst_range_start, dst_range_end = dst_start, dst_start + _len

        # dst_start, src_start, _len = [ int(x) for x in re.findall(r'\d+', line)]

        for x in init:
            x_start = x[0]
            x_end = x[1]
            # print("now running", x)
            if x_end < src_range_start:
                # print("in_smaller")

                local_mapping[x] = x
                pass
            elif x_start > src_range_end:
                # print("in_bigger")
                local_mapping[x] = x
                pass

            else:
                # if any([x_start > y[0] and x_end < y[1] for y in local_mapping.keys()]):
                #     print(x, "was already covered")
                #     continue
                # print("in_else")
                lower_bound = min(x_start, src_range_start)
                lower_limit = max(x_start, src_range_start)
                upper_limit = min(x_end, src_range_end)
                upper_bound = max(x_end, src_range_end)
                if dst_range_start + abs(src_range_start - lower_limit) == 0:
                    continue
                if lower_limit == 77:
                    print(dst_range_start)
                    print(src_range_start)
                    print(lower_bound, lower_limit)
                local_mapping[(lower_limit, upper_limit)] = (
                    dst_range_start + abs(src_range_start - lower_limit),
                    dst_range_end - abs(src_range_end - upper_limit),
                )
                # local_mapping[(upper_limit, upper_bound)] = (upper_limit, upper_bound)

            # print(local_mapping)
        # for dst_val, src_val in zip(range(dst_start, dst_start + _len), range(src_start, src_start + _len)):

        # print(index, init)
        # return 0
    init = list(local_mapping.values())
    # print(init)
    # print(min([x[0] for x in init]))
    print(index, init)
    # return 0
    return min([x[0] for x in init])


# 2427826 low
# 3427826 low
# 1209828
