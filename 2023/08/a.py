import networkx as nx
from regex import find_all_words


def custom_weight(f, t, meta):

    print(f, t)
    print(meta)

    print(f"Moved from {f} to {t}")
    return 1


def solve(example: list) -> int:
    ret_val = 0
    index = 0

    g = nx.MultiDiGraph()
    for i, line in enumerate(example[2:]):
        node, left, right = find_all_words(line)

        g.add_edge(node, left, key="L")
        g.add_edge(node, right, key="R")

    node = "AAA"
    ins = example[0]
    while True:
        LR = [x for x in g.neighbors(node)]
        if len(LR) == 1:
            node = LR[0]
        else:
            node = LR[0] if ins[index % len(ins)] == "L" else LR[1]
        index += 1
        if node == "ZZZ":
            break
    return index
