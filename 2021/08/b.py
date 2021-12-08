#!/usr/local/env python
from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as text:
    lines = [ line.strip() for line in text.read().split("\n") if line]

def find_all_uniques_in_list(solution: dict, _list:list):
    def find_unique(x: str):
        if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
            return len(x)
        return None
    for x in _list:
        unique = find_unique(x)
        if unique is not None:
            solution[unique] = x

def get_remainder(i: str, o: str):
    return [x for x in list(i) + list(o) if  x not in i]

def decipher(solution: dict, left: list):
    one = solution[2]
    seven = solution[3]
    four = solution[4]
    eight = solution[7]
    ret_str = ""
    for f in left:
        c_one = len(get_remainder(f, one))
        c_four = len(get_remainder(f, four))
        c_seven = len(get_remainder(f, seven))
        c_eight = len(get_remainder(f, eight))
        if c_one == 0 and c_four == 0 and c_seven == 0 and c_eight == 1:
            ret_str += "9"
        elif c_one == 1 and c_four == 1 and c_seven == 1 and c_eight == 1:
            ret_str += "6"
        elif c_one == 1 and c_four == 1 and c_seven == 1 and c_eight == 2:
            ret_str += "5"
        elif c_eight == 2 and c_seven == 0 and c_one == 0 and c_four == 1:
            ret_str += "3"
        elif c_eight == 2 and c_seven == 1 and c_one == 1 and c_four == 2:
            ret_str += "2"
        elif c_eight == 1 and c_four == 1 and c_seven == 0 and c_one == 0:
            ret_str += "0"
        elif c_eight == 5 and c_one == 0 and c_four == 2 and c_seven == 1:
            ret_str += "1"
        elif c_eight == 3 and c_four == 0 and c_seven == 1 and c_one == 0:
            ret_str += "4"
        elif c_eight == 4 and c_seven == 0 and c_one == 0 and c_four == 2:
            ret_str += "7"
        elif c_eight == 0:
            ret_str += "8"
        else:
            print(f, "---------")
            print(list(f) + list(one))
            print(one, c_one)
            print(four, c_four)
            print(seven, c_seven)
            print(eight, c_eight)
            exit(1)
    return int(ret_str)

def solve2(init_list: list) -> int:
    counter = 0
    solution = { k: "" for k in range(0,10)}
    for line in init_list:
        inp, outp = line.split(" | ")
        inputs = inp.split(" ")
        outputs = outp.split(" ")
        find_all_uniques_in_list(solution, inputs)
        find_all_uniques_in_list(solution, outputs)
        counter += decipher(solution, outputs)
    return counter



example = [ e.strip() for e in """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
""".split("\n") if e ]

simple_example = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]

spart2 = solve2(simple_example)
print('Example part 2:', spart2)
assert spart2 == 5353

part2 = solve2(example)
print('Example part 2:', part2)
assert part2 == 61229
print('Part 2:', solve2(lines))