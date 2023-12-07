import re
from typing import List


def find_all_int(line: str) -> List[int]:
    return [int(x) for x in re.findall(r"\d+", line)]
