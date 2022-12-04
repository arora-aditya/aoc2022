from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from statistics import *
from helper.submit import *
from utils import *


DAY = 4
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def part1(lines: List[str]) -> int:
    count = 0
    for line in lines:
        p1, p2 = line.split(",")
        p1s, p1e = p1.split("-")
        p1set = set(range(int(p1s), int(p1e) + 1))
        p2s, p2e = p2.split("-")
        p2set = set(range(int(p2s), int(p2e) + 1))
        if p1set.issubset(p2set) or p2set.issubset(p1set):
            count += 1
    return count


submit(1, part1(lines), force=False)


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    count = 0
    for line in lines:
        p1, p2 = line.split(",")
        p1s, p1e = p1.split("-")
        p1set = set(range(int(p1s), int(p1e) + 1))
        p2s, p2e = p2.split("-")
        p2set = set(range(int(p2s), int(p2e) + 1))
        if len(p1set & p2set) > 0:
            count += 1
    return count


submit(2, part2(lines), force=False)
