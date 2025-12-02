from typing import List

G_VISITED = []


def step(node: tuple, d: tuple) -> tuple:
    return (node[0] + d[0], node[1] + d[1])


def recr(example: list, node: tuple, direction: tuple) -> None:
    # print(node, direction, x, y)
    G_VISITED.append(node)

    while (
        (tmp := step(node, direction))
        and tmp[0] >= 0
        and tmp[1] >= 0
        and tmp[0] < len(example)
        and tmp[1] < len(example[0])
    ):
        G_VISITED.append(tmp)
        if G_VISITED.count(tmp) > 5:
            return
        # if tmp == (7,5):
        #     print(tmp, node, direction)
        next_char = example[tmp[0]][tmp[1]]
        if direction == (0, 1):  # right
            if next_char == "/":
                direction = (-1, 0)
            elif next_char == "\\":
                direction = (1, 0)
            elif next_char == "|":
                recr(example, tmp, (-1, 0))
                recr(example, tmp, (1, 0))
                return
            elif next_char in ["-", "."]:
                pass

        elif direction == (1, 0):  # down
            if next_char == "/":
                direction = (0, -1)
            elif next_char == "\\":
                direction = (0, 1)
            elif next_char == "-":
                recr(example, tmp, (0, -1))
                recr(example, tmp, (0, 1))
                return
            elif next_char in ["|", "."]:
                pass

        elif direction == (0, -1):  # left
            if next_char == "/":
                direction = (1, 0)
            elif next_char == "\\":
                direction = (-1, 0)
            elif next_char == "|":
                recr(example, tmp, (1, 0))
                recr(example, tmp, (-1, 0))
                return
            elif next_char in ["-", "."]:
                pass

        elif direction == (-1, 0):  # up
            if next_char == "/":
                direction = (0, 1)
            elif next_char == "\\":
                direction = (0, -1)
            elif next_char == "-":
                recr(example, tmp, (0, 1))
                recr(example, tmp, (0, -1))
                return
            elif next_char in ["|", "."]:
                pass
        node = tmp


def solve(example: List[str]) -> int:
    ret_val = 0
    h_matrix = []
    print("start")
    for y in range(len(example)):
        h_matrix.append([])
        for x in range(len(example[0])):
            h_matrix[y].append((y, x))
    node = (0, -1)
    direction = (0, 1)
    max_vals = []
    mm = len(h_matrix) * len(h_matrix[0])
    for i in range(len(h_matrix)):
        recr(example, (i, -1), (0, 1))
        print(i, 1, "/", mm)
        max_vals.append(get_n_clear(h_matrix))
        recr(example, (i, len(h_matrix)), (0, -1))
        print(i, 2, "/", mm)
        max_vals.append(get_n_clear(h_matrix))
        # print((i, -1))
        # print((i, len(h_matrix)))
    # print()
    for i in range(len(h_matrix[0])):
        # print((-1, i))
        # print((len(h_matrix[0]), i))
        recr(example, (-1, i), (1, 0))
        print(i, 3, "/", mm)
        max_vals.append(get_n_clear(h_matrix))
        recr(example, (len(h_matrix[0]), i), (-1, 0))
        print(i, 4, "/", mm)
        max_vals.append(get_n_clear(h_matrix))

    print("max_val", max(max_vals))
    return max(max_vals)


def get_n_clear(h_matrix) -> int:
    ret_val = 0
    for y in h_matrix:
        for x in y:
            # print("#" if x in G_VISITED else ".", end="")
            if x in G_VISITED:
                ret_val += 1
        # print()
    G_VISITED.clear()
    return ret_val
