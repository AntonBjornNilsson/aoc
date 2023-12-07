from typing import List
from collections import namedtuple

Cube = namedtuple("Cube", ["number", "color"])
limits = {"red": 12, "green": 13, "blue": 14}


def _find_local(current_game) -> bool:
    for set in current_game:
        for cube in set:
            if int(cube.number) > limits[cube.color]:
                return True
    return False


def solve(example: List[str]) -> int:
    data: List[List[Cube]] = []
    for _game in example:
        game = _game[_game.find(": ") + 2 :]

        data.append(
            [
                [Cube(*cube.split(" ")) for cube in set.split(", ")]
                for set in game.split("; ")
            ]
        )

    ret_val = 0
    for index in range(len(example)):
        current_game = data[index]
        if not _find_local(current_game):
            ret_val += index + 1

    return ret_val
