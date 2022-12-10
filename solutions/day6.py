from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from statistics import *
from helper.submit import *
from utils import *


DAY = 6
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def part1(lines: List[str]) -> int:
    line = lines[0].strip()
    start = 0
    for i in range(4, len(line)):
        if len(set(line[i - 4 : i])) == 4:
            return i


submit(1, part1(lines), force=True)


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    line = lines[0].strip()
    start = 0
    for i in range(14, len(line)):
        if len(set(line[i - 14 : i])) == 14:
            return i


submit(2, part2(lines), force=True)
