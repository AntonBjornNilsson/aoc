from typing import List


registrar = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solve(example: List[str]) -> int:
    total = []
    for line in example:
        val_str = [l if l.isdigit() else "" for l in line]

        for number in registrar.keys():
            search = True
            index = -1
            while search:
                f_index = line.find(number, index + 1)
                if f_index > -1:
                    val_str[f_index] = registrar[number]
                    index = f_index
                else:
                    break
        formatted_str = [s for s in val_str if s != ""]

        if len(formatted_str) == 1:
            formatted_str = formatted_str + formatted_str
        elif len(formatted_str) > 2:
            formatted_str = [formatted_str[0], formatted_str[-1]]
        total.append(int("".join(formatted_str)))
    return sum(total)
