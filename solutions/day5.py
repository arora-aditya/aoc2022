from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from parse import *
from pprint import pprint as pp
from math import *
from statistics import *
from helper.submit import *
from utils import *


DAY = 5
setup(DAY)
lines = read_file(DAY, strip=False)


# Part 1
##################################################
def part1(lines: List[str]) -> str:
    crates = defaultdict(list)
    for c, line in enumerate(lines[:8]):
        j = 0
        for i in range(0, len(line) + 1, 4):
            crate = line[i : i + 4].strip()
            j += 1
            if crate != "":
                crates[j].append(crate[1])
    for crate in crates:
        crates[crate] = crates[crate][::-1]

    for move in lines[10:]:
        move = move.split(" ")
        result = (int(move[1]), int(move[3]), int(move[5]))
        count, fro, to = result
        moved = crates[fro][-count:][::-1]
        for _ in range(count):
            crates[fro].pop()
        crates[to].extend(moved)

    ans = ""
    for i in range(1, 10):
        ans += crates[i][-1]

    return ans


submit(1, part1(lines), force=False)


# Part 2
##################################################
def part2(lines: List[str]) -> str:
    crates = defaultdict(list)
    for c, line in enumerate(lines[:8]):
        j = 0
        for i in range(0, len(line) + 1, 4):
            crate = line[i : i + 4].strip()
            j += 1
            if crate != "":
                crates[j].append(crate[1])
    for crate in crates:
        crates[crate] = crates[crate][::-1]

    for move in lines[10:]:
        move = move.split(" ")
        result = (int(move[1]), int(move[3]), int(move[5]))
        count, fro, to = result
        moved = crates[fro][-count:]
        for _ in range(count):
            crates[fro].pop()
        crates[to].extend(moved)
    ans = ""
    for i in range(1, 10):
        ans += crates[i][-1]

    return ans


submit(2, part2(lines), force=False)
