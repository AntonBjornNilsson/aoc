from pathlib import Path
from aocd.models import Puzzle


def validate(_path, example1=None, example2=None, answer1=None, answer2=None):
    path = Path(_path)
    year = int(path.parent.parent.name)
    day = int(path.parent.name)
    puzzle = Puzzle(year=year, day=day)
    solution1 = puzzle.examples[0].answer_a
    solution2 = puzzle.examples[0].answer_b
    try:
        solution1 = int(solution1)
        solution2 = int(solution2)
    except:
        pass

    if example1 is not None:
        assert type(solution1) == type(example1)
        if solution1 != example1:
            print(
                f"Incorrect answer to example 1: Should be {solution1} but was {example1}"
            )
            exit(1)

    if answer1 is not None:
        print("Part 1:", answer1)

    if puzzle.answered_a:
        if example2 is not None:
            assert type(solution2) == type(example2)
            if solution2 != example2:
                print(
                    f"Incorrect answer to example 2: Should be {solution2} but was {example2}"
                )
                exit(1)

        if answer2 is not None:
            print("Part 2:", answer2)
