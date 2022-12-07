#!/usr/local/env python
from pathlib import Path
import re
from collections import defaultdict

with (Path(__file__).parent / "input.txt").open() as text:
    lines = [ line.strip() for line in text.read().split("\n") if line]


def solve(init_list: list) -> int:
    context = "/"
    mode = "step"
    dir_count = defaultdict(lambda: 0)
    for command in init_list[1:]:
        if "$" in command:
            if "cd" in command:
                mode = "step"
                if ".." in command:
                    context = "/".join(context.split("/")[:-1]) if context.count("/") > 1 else "/"
                else:
                    context += "/" + command[5:] if context[-1] != "/" else command[5:]
            if command == "$ ls":
                mode = "read"
        if mode == "read" and "dir" not in command:
            size = re.findall(r'\d+', command)
            if size:
                for slashes in range(context.count("/")+1):
                    temp = "/" + "/".join(context[1:].split("/")[:slashes])
                    dir_count[temp] += int(size[0])
    ret = 0
    for k, v in dir_count.items():
        if v < 100000:
            ret += v
        print(k, v)
    return ret


# def solve2(init_list: list) -> int:



example = [ e.strip() for e in """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".split("\n") if e ]


part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 95437
print("Part 1:", solve(lines))
