from typing import List

def prep(example: List[str]) -> List[str]:

    rows_i = []
    cols_i = []
    for i, line in enumerate(example):
        if line == '.' * len(line):
            rows_i.append(i)
    for col in range(len(example[0])):
        cols = [example[x][col] for x in range(len(example))]
        if cols == ["."] * len(cols):
            cols_i.append(col)

    extendo = 1
    new_ex = []
    for x in range(len(example)):
        new_ex.append([])
        for y in range(len(example[0])):
            new_ex[x].append((x,y))

    for r in rows_i:
        for row in range(r, len(example)):
            new_ex[row] = [(x[0]+extendo, x[1]) for i, x in enumerate(new_ex[row])]

    for r in cols_i:
        for row in range(len(example)):
            new_ex[row] = [(x[0], x[1]) if i <= r else (x[0], x[1] + extendo)  for i, x in enumerate(new_ex[row])]


    return new_ex
def abs_pnt(x, y) -> int:
    return max(x[0], y[0]) - min(x[0], y[0]) + max(x[1], y[1]) - min(x[1], y[1])

def solve(example: List[str]) -> int:
    new_ex = prep(example)
    num = []
    for row in range(len(example)):
        for col in range(len(example[0])):
            if example[row][col] == "#":
                num.append((row, col))

    ret_val = 0

    for i, n in enumerate(num):
        shps = [abs_pnt(new_ex[n[0]][n[1]], new_ex[x[0]][x[1]]) for x in num if n != x and num.index(x) > i]
        ret_val += sum(shps)

    return ret_val

# 9957702