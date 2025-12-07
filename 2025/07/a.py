from typing import List

visited = []


def recr(grid: list, pos: list[int, int], splits: list) -> int:
    if pos[0] + 1 == len(grid) - 1:
        return splits
    for iy in range(pos[0] + 1, len(grid)):
        if grid[iy][pos[1]] == "^":
            if (iy, pos[1]) not in splits:
                splits.append((iy, pos[1]))
            for new in [[iy, pos[1] - 1], [iy, pos[1] + 1]]:

                if new not in visited:
                    visited.append(pos)
                    for n in recr(grid, new, []):
                        if n not in splits:
                            splits.append(n)

            return splits
    return splits


def solve(example: List[str]) -> int:
    grid = []
    splits = []
    start = [0, 0]
    global visited
    visited = []
    for iy, line in enumerate(example):
        grid.append([char for char in line])
        if "S" in line:
            start = [iy, line.index("S")]

    splits = recr(grid, start, [])

    return len(set(splits))


# 1560 correct
