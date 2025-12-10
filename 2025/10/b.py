from copy import deepcopy
from typing import List
from regex import find_all_in_paranthesis, find_all_in_curly_brackets


def mul(state: list, button: list) -> list:
    return [ a + b for a, b in zip(state, button)]

def check_progress(goal: list, new: list) -> bool:
    # print(goal, new, "cheking")
    good = [b - a for a, b in zip(new, goal)]
    if any(x < 0 for x in good):
        return False
    return True



def solve(example: List[str]) -> int:
    ret_val = 0

    for i, line in enumerate(example, 1):
        print("current line", line)
        num_lights = line.count(".") + line.count("#")
        # states = [False for _ in range(num_lights)]
        states = [0 for _ in range(len(find_all_in_curly_brackets(line)[0].split(",")))]
        goal = [int(x) for x in find_all_in_curly_brackets(line)[0].split(",")]
        buttons = [
            [1 if str(y) in x.split(",") else 0 for y in range(num_lights)] for x in find_all_in_paranthesis(line)
        ]
        # print(states, buttons, goal, "goal")
        global smallest_solution 
        smallest_solution = 99999

        visited = []
        def recr(state: list, current: list) -> None:
            # print(state, goal, depth)
            
            if current not in visited:
                # print(state, button)
                visited.append(current)
                # print("addin", current)
            else:
                return
            if state == goal:
                print(state, "FOUND!!!!!!!!")
                global smallest_solution
                if sum(current) <= smallest_solution:
                    smallest_solution = sum(current)
                return

            for i, button in enumerate(buttons):
                new_state = mul(state, button)
                assert new_state != state
                n_current = deepcopy(current)
                n_current[i] += 1
                
                if check_progress(goal, new_state):
                    # print("found progress", state, "->", new_state)
                    recr(new_state, n_current)
        recr(states, [0 for _ in range(len(buttons))])
        # print(visited)
        ret_val += smallest_solution
        print(i, smallest_solution)
    return ret_val

# 527