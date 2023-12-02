from pathlib import Path
from parsers import parse_raw
from validation import validate
from .a import solve
from .b import solve as solve2

parse_function = parse_raw

lines = parse_function(__file__, "input")
ex_lines_a = parse_function(__file__, "example_a")
# example b needs to be created manually if it exists
ex_lines_b = (
    parse_function(__file__, "example_b")
    if (Path(__file__).parent / "example_b.txt").is_file()
    else ex_lines_a
)

example_a = solve(ex_lines_a)
validate(__file__, example1=example_a)
solution_a = solve(lines)
validate(__file__, answer1=solution_a)
example_b = solve2(ex_lines_b)
validate(__file__, example2=example_b)
solution_b = solve2(lines)
validate(__file__, answer2=solution_b)
