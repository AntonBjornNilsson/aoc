#!/usr/local/env python
import argparse
from datetime import date
from pathlib import Path
import sys
from typing import Tuple

import aocd
from bs4 import BeautifulSoup
import requests

#####################################################################
# Setup
#####################################################################
today_date = int(date.today().strftime("%d"))
today_year = int(date.today().strftime("%Y"))
if len(sys.argv) > 1:
    #####################################################################
    # Argparse, mutually exclusive due to multiple argparse in program
    #####################################################################
    parser = argparse.ArgumentParser(description='Rise and shine, today is a new day')
    parser.add_argument('--day', type=int, default=today_date,
                        help='What day is it')
    parser.add_argument('--year', type=int, default=today_year,
                        help='What year is it')
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
# Create folders
#####################################################################
print(f"Setting up a folder for {day} - {year}")
directory = (Path(str(year)) / str(day).zfill(2)).resolve()
print(f"In directory {directory}")
directory.mkdir(parents=True, exist_ok=True)

#####################################################################
# Get input.txt
#####################################################################
puzzle = aocd.models.Puzzle(year=year, day=day)
input_txt = directory / 'input.txt'
input_txt.write_text(puzzle.input_data, "utf8")
is_part_a_done = puzzle.answered_a
is_part_b_done = puzzle.answered_b

#####################################################################
# Scrape daily challenge, functions
#####################################################################
def parse_from_web():
    print("parsed scrape from web")
    cookies = {"session": session_cookie }
    url = f"https://adventofcode.com/{year}/day/{day}"
    response = requests.get(url, cookies=cookies)
    assert response.status_code == 200, f"{url} returned a bad response"
    html_string = response.text
    scrape_path.parent.mkdir(exist_ok=True, parents=True)
    scrape_path.write_text(html_string)
    return html_string

def parse_html(html_string: str) -> Tuple[str, int, int]:
    soup = BeautifulSoup(html_string, 'html5lib')
    articles = soup.find_all("article")
    first_part = articles[0]
    element_pre = first_part.find("pre")
    element_answer = first_part.find_all("p")[-2].find_all("em")[-1]
    example_input = element_pre.get_text()
    answer = element_answer.get_text()
    try:
        second_part = articles[1]
        element_answer2 = second_part.find_all("p")[-2].find_all("em")[-1]
        answer2 = element_answer2.get_text()
    except:
        answer2 = -1
    return example_input, answer, answer2

#####################################################################
# Scrape daily challenge
#####################################################################
session_cookie = (Path(aocd.models.AOCD_CONFIG_DIR) / "token").read_text()
scrape_path: Path = (Path(aocd.models.AOCD_DATA_DIR) / "bs4" / str(year) / str(day))
scrape_path = scrape_path / "a" if not is_part_a_done else scrape_path / "b"
if scrape_path.is_file():
    print("parsed scrape from cache")
    html_string = scrape_path.read_text()
else:
    html_string = parse_from_web()
example_input, answer, answer2 = parse_html(html_string)

a_py = directory / "a.py"
b_py = directory / "b.py"
if not is_part_a_done:
    #####################################################################
    # Create a.py
    #####################################################################
    template_path = Path("template.py")
    template_data = template_path.read_text()
    template_data = template_data.replace("<example_string>", example_input)
    template_data = template_data.replace("<answer_string>", answer)
    a_py.write_text(template_data)
    print("Run with command:")
    print()
    print(f"python {year}/{str(day).zfill(2)}/a.py")
elif not is_part_b_done:
    #####################################################################
    # Create b.py
    #####################################################################
    temp_py = a_py.read_text().split('\n')
    # copy solve function
    solve_string = "def solve(init_list: list) -> int:"
    solve2_string = "# def solve2(init_list: list) -> int:"
    solve_index = temp_py.index(solve_string)
    solve2_index = temp_py.index(solve2_string)
    solve_closed = temp_py.index('', solve_index)

    temp_py[solve2_index:solve2_index] = temp_py[solve_index:solve_closed]
    temp_py[solve2_index] = temp_py[solve2_index].replace("solve", "solve2")
    temp_py.remove(solve2_string)

    temp_py.extend([
        "part2 = solve2(example)",
        "print('Example part 2:', part2)",
        f"assert part2 == {answer2}",
        "print('Part 2:', solve2(lines))",
    ])

    b_py.write_text("\n".join(temp_py))
    print("Run with command:")
    print()
    print(f"python {year}/{str(day).zfill(2)}/b.py")
else:
    print("Both part A and B are completed. Nothing to do here")
