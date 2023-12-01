def solve(example: list) -> int:
    total = []
    for line in example:
        val_str = "".join([l for l in line if l.isdigit()])
        if len(val_str) == 1:
            val_str = val_str + val_str
        elif len(val_str) > 2:
            val_str = val_str[0] + val_str[-1]
        total.append(int(val_str))

    return sum(total)
