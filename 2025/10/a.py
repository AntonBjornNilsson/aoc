from typing import List
from regex import find_all_in_paranthesis
from copy import deepcopy


def mul(state: list, button: list) -> list:
    return [not a if b is True else a for a, b in zip(state, button)]


def solve(example: List[str]) -> int:
    ret_val = 0

    for i, line in enumerate(example, 1):
        print("current line", line)
        num_lights = line.count(".") + line.count("#")
        states = [False for _ in range(num_lights)]
        goal = [line[x] == "#" for x in range(1, num_lights + 1)]
        buttons = [
            [str(y) in x.split(",") for y in range(num_lights)]  for x in find_all_in_paranthesis(line)
        ]
        # print(states, goal)
        # print(buttons)
        global smallest_solution 
        smallest_solution = 8


        def recr(state: list, depth: int = -1) -> None:
            depth += 1
            # print(state, goal, depth)
            if state == goal:
                global smallest_solution
                smallest_solution = depth
                return
            if depth >= smallest_solution:
                return
            for button in buttons[::-1]:
                recr(mul(deepcopy(state), button), depth)

        recr(deepcopy(states))

        ret_val += smallest_solution
        print(i, smallest_solution)
    return ret_val

# 527