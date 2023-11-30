from pathlib import Path


def parse_int_on_newline(file: str, filename: str, formatted: bool = False):
    lines = parse_raw(file, filename, formatted)

    lines = [int(line) if line else None for line in lines]

    return lines


def parse_raw(file: str, filename: str, formatted: bool):
    lines = [
        line.strip()
        for line in (Path(file).parent / f"{filename}.txt").open().readlines()
    ]
    if formatted:
        lines = [line for line in lines if line]
    return lines
