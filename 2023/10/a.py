from typing import List
import networkx as nx
import sys
# sys.setrecursionlimit(25000)

s = ['S']
from_west = ['-', '7', 'J'] + s
from_east = ['-', 'L', 'F'] + s
from_north = ['|', 'J', 'L'] + s
from_south = ['|', '7', 'F'] + s

def build_graph(graph: nx.graph.Graph, example:list, node: tuple) -> None:
    # graph.add_node(node)
    row, col = node
    if row >= len(example) or col >= len(example[0]) or row < 0 or col < 0:
        print(row, col)
        return
    # print("add recr for ", node, example[row][col])
    if row > 0 and example[row-1][col] in from_south:
        north = (row-1, col)
        if (node, north) not in graph.edges():
            # print("Found north")
            graph.add_edge(node, north)
            build_graph(graph, example, north)
    if col > 0 and example[row][col-1] in from_east:
        west = (row, col-1)
        if (node, west) not in graph.edges():
            # print("Found west")
            graph.add_edge(node, west)
            build_graph(graph, example, west)
    if col < len(example[0]) - 1 and example[row][col+1] in from_west:
        east = (row, col+1)
        if (node, east) not in graph.edges():
            # print("Found east")
            graph.add_edge(node, east)
            build_graph(graph, example, east)
    if row < len(example) - 1 and example[row+1][col] in from_north:
        south = (row +1, col)
        if (node, south) not in graph.edges():
            # print("Found south")
            graph.add_edge(node, south)
            build_graph(graph, example, south)

    # if example[row][col] == "S":
    #     print("Found s in", node)
    #     print("east", example[row][col+1])
    #     print("south", example[row+1][col])
    #     print("west", example[row][col-1])
    #     print("north", example[row-1][col])

def solve(example: List[str]) -> int:
    ret_val = 0
    start = (0,0)
    for x, line in enumerate(example):
        # print(x, line)
        for y,col in enumerate(line):
            if col == "S":
                start = (x, y)

    graph = nx.graph.Graph()
    build_graph(graph, example, start)
    print(graph.nodes())

    print("len nodes pre trim", len(graph.nodes()))

    # print(nx.depth_first_search.dfs_tree(graph, start))
    print("calc diameter")
    return nx.diameter(graph)
