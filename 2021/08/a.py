#!/usr/local/env python
from pathlib import Path


with (Path(__file__).parent / "input.txt").open() as text:

    lines = [line.strip() for line in text.read().split("\n") if line]


def solve(init_list: list) -> int:
    counter = 0
    possibe = ("a", "b", "c", "d", "e", "f", "g")
    for line in init_list:
        inp, outp = line.split(" | ")
        inputs = inp.split(" ")
        outputs = outp.split(" ")
        for x in outputs:
            if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
                counter += 1
    return counter


# def solve2(init_list: list) -> int:


example = [
    e.strip()
    for e in """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
""".split(
        "\n"
    )
    if e
]


part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 26
print("Part 1:", solve(lines))
