from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from statistics import *
from helper.submit import *
from utils import *


DAY = 1
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def part1(lines: List[str]) -> int:
    lines = read_file(DAY)
    elves = []
    elf_sum = 0
    for line in lines:
        if line == "":
            elves.append(elf_sum)
            elf_sum = 0
        else:
            elf_sum += int(line)
    if elf_sum != 0:
        elves.append(elf_sum)
    return max(elves)


submit(1, part1(lines), force=False)


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    lines = read_file(DAY)
    elves = []
    elf_sum = 0
    for line in lines:
        if line == "":
            elves.append(elf_sum)
            elf_sum = 0
        else:
            elf_sum += int(line)
    if elf_sum != 0:
        elves.append(elf_sum)
    return sum(list(sorted(elves, reverse=True))[0:3])


submit(2, part2(lines), force=False)
