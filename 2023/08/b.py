import math

import networkx as nx
from regex import find_all_words


def custom_weight(f, t, meta):

    print(f, t)
    print(meta)

    print(f"Moved from {f} to {t}")
    return 1


def solve(example: list) -> int:
    index = 0

    g = nx.MultiDiGraph()
    for _, line in enumerate(example[2:]):
        node, left, right = find_all_words(line)

        g.add_edge(node, left, key="L")
        g.add_edge(node, right, key="R")

    start_nodes = [x for x in g.nodes() if x[2] == "A"]

    ins = example[0]
    res_list = [[] for _ in range(len(start_nodes))]
    while True:
        local_nodes = []
        for node in start_nodes:
            LR = [x for x in g.neighbors(node)]
            if len(LR) == 1:
                _node = LR[0]
            else:
                _node = LR[0] if ins[index % len(ins)] == "L" else LR[1]
            local_nodes.append(_node)
        index += 1
        if any(x[-1] == "Z" for x in local_nodes):
            for x in local_nodes:
                if x[-1] == "Z":
                    res_list[local_nodes.index(x)].append(index)
                    print(index, x, local_nodes.index(x))
        if all(len(x) > 2 for x in res_list):
            break

        start_nodes = local_nodes

    res = [x[1] - x[0] for x in res_list]

    return math.lcm(*res)
