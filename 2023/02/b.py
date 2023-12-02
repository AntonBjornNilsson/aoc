from typing import List
from collections import namedtuple
import math

Cube = namedtuple("Cube", ["number", "color"])
limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}
def _find_local(current_game) -> bool:

    local = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for set in current_game:
        for cube in set:
            local[cube.color] = max(local[cube.color], int(cube.number))
    return math.prod(local.values())


def solve(example: List[str]) -> int:
    data: List[List[Cube]] = []
    for _game in example:
        game = _game[_game.find(": ")+2:]

        data.append([[Cube(*cube.split(" ")) for cube in set.split(", ")] for set in game.split("; ")])

    ret_val = 0
    for index in range(len(example)):
        current_game = data[index]
        ret_val += _find_local(current_game)
    return ret_val