#!/usr/local/env python
from pathlib import Path
import networkx as nx

with (Path(__file__).parent / "input.txt").open() as text:

    lines = [line.strip() for line in text.read().split("\n") if line]


def solve(init_list: list) -> int:
    ret = 0
    height_map = []
    graph = nx.Graph()

    start = None
    stop = None
    for i, line in enumerate(init_list):
        print(line)
        height_map.append([])
        for char_i, char in enumerate(line):
            char_value = ord(char)
            if char == "S":
                start = (i, char_i)
                char_value = ord("a")
            if char == "E":
                stop = (i, char_i)
                char_value = ord("z") + 1

            print(char_value)
            height_map[i].append(char_value - ord("a"))
            graph.add_node((i, char_i))

    for line in height_map:
        print(line)
    cols = len(height_map[0]) - 1
    rows = len(height_map) - 1
    for node in graph.nodes():
        x, y = node
        if x > 0:
            graph.add_edge(node, (x - 1, y), weight=height_map[x - 1][y])
        if x < rows:
            graph.add_edge(node, (x + 1, y), weight=height_map[x + 1][y])
        if y > 0:
            graph.add_edge(node, (x, y - 1), weight=height_map[x][y - 1])
        if y < cols:
            graph.add_edge(node, (x, y + 1), weight=height_map[x][y + 1])

    print(graph.nodes())
    print(graph.edges(data=True))

    def custom_weight(f, t, meta):
        f1, f2 = f
        t1, t2 = t
        # print(f1, f2)
        # print(t1, t2)
        # print(meta)
        print(
            height_map[f1][f2],
            height_map[t1][t2],
            height_map[f1][f2] - height_map[t1][t2],
        )
        if height_map[t1][t2] - height_map[f1][f2] > 1:
            return None
        print(f"Moved from {f} to {t}")
        return 1

    # nx_ret = nx.dijkstra_path(graph, (0,0), (2,5), weight=custom_weight)
    nx_ret = nx.shortest_path(graph, start, stop, weight=custom_weight)
    print(nx_ret)
    print(len(nx_ret))
    return len(nx_ret) - 1


example = [
    e.strip()
    for e in """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split(
        "\n"
    )
    if e
]


part2 = solve(example)
print("Example part 1:", part2)
assert part2 == 31
print("Part 1:", solve(lines))

# 456 correct
# Du fattar inte hur glad jag blev
