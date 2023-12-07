from collections import defaultdict
from typing import Tuple
from functools import cmp_to_key

val_mapping = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def _type_and_high(hand: str) -> Tuple[int, int]:
    chars = {}
    while True:
        char = hand[0]
        val_char = val_mapping
        if val_char[char] not in chars:
            chars[val_char[char]] = hand.count(char)

        hand = hand[1:]
        if not hand:
            break
    highest = max(chars.keys())
    _type = 0
    kinds = list(chars.values())

    if 5 in kinds:
        _type = 7
    elif 4 in kinds:
        _type = 6
    elif 3 in kinds and 2 in kinds:
        _type = 5
    elif 3 in kinds:
        _type = 4
    elif len([x for x in kinds if x == 2]) == 2:
        _type = 3
    elif 2 in kinds:
        _type = 2
    elif len(kinds) == 5:
        _type = 1
    else:
        raise
    return _type, highest


def sort_func(i1: str, i2: str) -> int:
    for x, y in zip(i1, i2):
        if x == y:
            continue
        return val_mapping[x] - val_mapping[y]


def solve(example: list) -> int:
    ret_val = 0
    hands = []
    bids = {}
    for i, line in enumerate(example):
        hand = line[:5]
        bid = line[6:]
        hands.append(hand)
        bids[hand] = int(bid)

    local_mapping = defaultdict(lambda: [])
    for i, hand in enumerate(hands):
        rank, high = _type_and_high(hand)
        local_mapping[rank].append(hand)
    final = []
    for _ in range(len(local_mapping.keys())):
        smallest = min(local_mapping.keys())
        vals = local_mapping.pop(smallest)
        sorted_vals = sorted(vals, key=cmp_to_key(sort_func), reverse=False)
        final.extend(sorted_vals)

    for i, hand in enumerate(final):
        ret_val += (i + 1) * bids[hand]

    return ret_val
