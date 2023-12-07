from regex import find_all_int
import math


def solve(example: list) -> int:
    ret_val = []
    times = find_all_int(example[0])
    dists = find_all_int(example[1])

    for time, dist in zip(times, dists):
        local_wins = 0
        for held_time in range(0, time + 1):
            time_pen = held_time
            trav_time = time - time_pen
            this_dist = trav_time * held_time
            if this_dist > dist:
                local_wins += 1
        ret_val.append(local_wins)
    return math.prod(ret_val)
