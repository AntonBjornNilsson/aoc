def solve(example: list) -> int:
    ret_dict = {x: 1 for x in range(len(example))}
    for i, line in enumerate(example):
        val_line = line[8:].strip()
        w, h = val_line.split("|")
        wins = [w for w in w.split(" ") if w]
        hands = [l for l in h.split(" ") if l]
        local_wins = 0
        for h in hands:
            if h in wins:
                local_wins += 1

        for x in range(local_wins):
            ret_dict[i + 1 + x] += ret_dict[i]

    return sum(ret_dict.values())
