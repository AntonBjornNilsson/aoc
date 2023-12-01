from parsers import parse_int_on_newline, parse_raw
from validation import validate
from .a import solve
from .b import solve as solve2

parse_function = parse_raw

lines = parse_function(__file__, "input")
example = parse_function(__file__, "example")
example2 = parse_function(__file__, "example2")
print(f"Formatted example looks like this \n{example}")
example_a = solve(example)
solution_a = solve(lines)
example_b = solve2(example2)
solution_b = solve2(lines)

validate(__file__, example_a, example_b, solution_a, solution_b)
