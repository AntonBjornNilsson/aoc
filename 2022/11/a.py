#!/usr/local/env python
from dataclasses import dataclass
from pathlib import Path
import re
from typing import List, Union


with (Path(__file__).parent / "input.txt").open() as text:

    lines = [line.strip() for line in text.read().split("\n") if line]


@dataclass
class Monkey:
    items: List[int]
    first: Union[str, int]
    second: Union[str, int]
    ops: Union[str, int]
    div: int
    if_true: int
    if_false: int
    increment: int = 0

    def __str__(self):
        return f"Monkey holding {self.items} items"

    def increase_worry(self, item_index):
        f = self.first
        s = self.second
        print(self.items, item_index)
        if self.first == "old":
            f = self.items[item_index]
        if self.second == "old":
            s = self.items[item_index]
        if "+" in self.ops:
            self.items[item_index] = f + s
            print("item inc to", self.items[item_index])
            return
        if "*" in self.ops:
            self.items[item_index] = f * s
            print("item inc to", self.items[item_index])
            return
        raise Exception(f"{self.ops} is not implemented {repr(self)}")

    def incr_inspect(self):
        self.increment += 1

    def decrease_worry(self, item_index):
        self.items[item_index] = self.items[item_index] // 3
        print("item dec to", self.items[item_index])

    def test(self, item_index):
        return self.items[item_index] % self.div == 0

    def next_monkey(self, item_index):
        is_true = self.test(item_index)
        return self.if_true if is_true else self.if_false


def setup_monkeys(_list):
    monkeys = []

    start = [_list[x] for x in range(1, len(_list), 6)]
    operation = [_list[x] for x in range(2, len(_list), 6)]
    test = [_list[x] for x in range(3, len(_list), 6)]
    tr = [_list[x] for x in range(4, len(_list), 6)]
    fl = [_list[x] for x in range(5, len(_list), 6)]

    for s, o, t, tt, ff in zip(start, operation, test, tr, fl):
        start_items = [int(x) for x in re.findall("\d+", s)]
        first, ops, second = re.findall("\w+...\w+", o)[-1].split(" ")
        first = int(first) if first.isdigit() else first
        second = int(second) if second.isdigit() else second
        div = int(re.findall("\d+", t)[0])
        tru = int(re.findall("\d+", tt)[0])
        fls = int(re.findall("\d+", ff)[0])
        monkey = Monkey(start_items, first, second, ops, div, tru, fls)
        monkeys.append(monkey)

    return monkeys


def solve(init_list: list) -> int:
    monkeys: List[Monkey] = setup_monkeys(init_list)
    for round in range(20):
        for monkey in monkeys:
            print("new monkey")
            while (len(monkey.items)) > 0:
                print("new item")
                item_index = 0
                monkey.incr_inspect()
                monkey.increase_worry(item_index)
                monkey.decrease_worry(item_index)
                next_m = monkey.next_monkey(item_index)
                item = monkey.items.pop(item_index)
                monkeys[next_m].items.append(item)
    for monkey in monkeys:
        print(monkey)
    for monkey in monkeys:
        print(f"Monkey 0 inspected items {monkey.increment} times")
    monkey_inspects = [monkey.increment for monkey in monkeys]
    most = max(monkey_inspects)
    monkey_inspects.remove(most)
    s_most = max(monkey_inspects)
    return most * s_most


# def solve2(init_list: list) -> int:


example = [
    e.strip()
    for e in """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".split(
        "\n"
    )
    if e
]


part1 = solve(example)
print("Example part 1:", part1)
assert part1 == 10605
print("Part 1:", solve(lines))

# 111210 correct
