from functools import reduce
import operator
from typing import List
from dataclasses import InitVar, dataclass, field
import math
import numpy as np


@dataclass
class Junk:
    x: int
    y: int
    z: int
    array: np.array = field(init=False)
    closest: list[tuple[float, int]] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.array = np.array([self.x, self.y, self.z])

    def euq_dist(self, other: "Junk") -> float:
        if self is other:
            return float(10**9)
        p1 = self.array
        p2 = other.array

        squared_dist = np.sum((p1 - p2) ** 2, axis=0)
        dist = np.sqrt(squared_dist)
        return float(dist)

    def __str__(self) -> str:
        return f"({self.x},{self.y},{self.z})"

    def __repr__(self):
        return str(self)


def solve(example: List[str]) -> int:
    junk_list: list[Junk] = []

    # x = Junk(162,817,812)
    # y = Junk(425,690,689)
    # z = Junk(431,825,988)

    # print("x->y", x.euq_dist(y))
    # print("x->z", x.euq_dist(z))

    # print("y->x", y.euq_dist(x))
    # print("y->z", y.euq_dist(z))

    # print("z->x", z.euq_dist(x))
    # print("z->y", z.euq_dist(y))
    # return 0

    for i, line in enumerate(example):
        junk_list.append(Junk(*[int(x) for x in line.split(",")]))

    for j in junk_list:
        dist_to_all = [(j.euq_dist(jj), index) for index, jj in enumerate(junk_list)]
        j.closest = sorted(dist_to_all, key=lambda x: x[0])

        # print(j, "is closest to", junk_list[j.closest_index])

    order_list = sorted(junk_list, key=lambda x: x.closest[0][0])
    ret_list = []

    for j in order_list[:10]:
        print("looking at", j)

        while len(j.closest) > 0:
            should_add = True
            _, index = j.closest.pop(0)
            closest_j = junk_list[index]
            print("closest is", closest_j)
            for r in ret_list:
                if closest_j in r:
                    print("r", closest_j, "was aleady in list")
                    if j not in r:
                        r.append(j)
                    should_add = False

                    break
            if should_add:
                print(j, "is closest to", closest_j)
                ret_list.append([j, closest_j])
                break

    sort_ret = sorted(ret_list, key=lambda x: len(x), reverse=True)
    for i in sort_ret:
        print(len(i), i)
    return 0
    return reduce(operator.mul, [len(x) for x in sort_ret[:3]])
