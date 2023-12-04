
def solve(example: list) -> int:
    ret_val = 0
    for line in example:
        val_line = line[8:].strip()
        w, h = val_line.split("|")
        wins = [w for w in w.split(" ") if w]
        hands = [l for l in h.split(" ") if l]
        local_wins = -1
        for h in hands:
            if h in wins:
                local_wins += 1
        if local_wins > -1:
            ret_val = ret_val + 2**local_wins

    return ret_val
