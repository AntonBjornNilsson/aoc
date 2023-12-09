#!/usr/local/env python
import argparse
from datetime import date
from pathlib import Path
import sys

import aocd

#####################################################################
# Setup
#####################################################################
today_date = int(date.today().strftime("%d"))
today_year = int(date.today().strftime("%Y"))
if len(sys.argv) > 1:
    #####################################################################
    # Argparse, mutually exclusive due to multiple argparse in program
    #####################################################################
    parser = argparse.ArgumentParser(description="Rise and shine, today is a new day")
    parser.add_argument("--day", type=int, default=today_date, help="What day is it")
    parser.add_argument("--year", type=int, default=today_year, help="What year is it")
    p = parser.parse_args()
    day: int = p.day
    year: int = p.year
else:
    day = today_date
    year = today_year
    #####################################################################
    # Scrape valid aoc token from browser cookies
    #####################################################################
    # It works, crazy :D
    aocd.cookies.scrape_session_tokens()


#####################################################################
# Create folders and init
#####################################################################
print(f"Setting up a folder for {day} - {year}")
directory = (Path(str(year)) / str(day).zfill(2)).resolve()
print(f"In directory {directory}")
directory.mkdir(parents=True, exist_ok=True)
year_init = directory.parent / "__init__.py"
day_init = directory / "__init__.py"
year_init.touch(exist_ok=True)
day_init.touch(exist_ok=True)

#####################################################################
# Get input.txt
#####################################################################
puzzle = aocd.models.Puzzle(year=year, day=day)
input_txt = directory / "input.txt"
input_txt.write_text(puzzle.input_data, "utf8")

example_input = puzzle.examples[0].input_data
answer = puzzle.examples[0].answer_a
answer2 = puzzle.examples[0].answer_b
extra = puzzle.examples[0].extra

a_example = directory / "example_a.txt"
b_example = directory / "example_extra.txt"
a_example.write_text(example_input)
if extra:
    b_example.write_text(extra)
is_part_a_done = puzzle.answered_a
is_part_b_done = puzzle.answered_b

#####################################################################
# Scrape daily challenge
#####################################################################

run_py = directory / "run.py"
a_py = directory / "a.py"
b_py = directory / "b.py"
template_path = Path("template.py")
template_data = template_path.read_text()
if not run_py.is_file():
    run_py.write_text(template_data)


#####################################################################
# Create a.py
#####################################################################
template_path = Path("template.py")
template_data = """from typing import List

def solve(example: List[str]) -> int:
    ret_val = 0
    for i, line in enumerate(example):
        pass

    return ret_val
"""
if not a_py.is_file():
    a_py.write_text(template_data)


#####################################################################
# Create b.py
#####################################################################

if not b_py.is_file() or not is_part_b_done:
    b_py.write_text(a_py.read_text())
print("Run with command:")
print()
print(f"python -m {year}.{str(day).zfill(2)}.run")
