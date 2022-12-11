from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from statistics import *
from parse import *
from helper.submit import *
from utils import *


DAY = 10
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def increment_cycle(x, cycle_number, su):
    cycle_number += 1
    if cycle_number % 40 == 20:
        su += cycle_number * x
    return cycle_number, su


def part1(lines: List[str]) -> int:
    x = 1
    cycle_number = 0
    su = 0
    for line in lines:
        if line[0] == "a":
            cycle_number, su = increment_cycle(x, cycle_number, su)
            inst = parse("addx {:d}", line.strip())[0]
            cycle_number, su = increment_cycle(x, cycle_number, su)
            x += inst
        else:
            cycle_number, su = increment_cycle(x, cycle_number, su)
    return su


submit(1, part1(lines), force=False)


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    l = []

    def increment_cycle(x, cycle_number):
        char = "#" if (x - 1 <= (cycle_number % 40) <= x + 1) else "."
        l.append(char)
        cycle_number += 1
        return cycle_number

    x = 1
    cycle_number = 0
    su = 0
    for line in lines:
        if line[0] == "a":
            cycle_number = increment_cycle(x, cycle_number)
            inst = parse("addx {:d}", line.strip())[0]
            cycle_number = increment_cycle(x, cycle_number)
            x += inst
        else:
            cycle_number = increment_cycle(x, cycle_number)
    pp("".join(l[:40]))
    pp("".join(l[40:80]))
    pp("".join(l[80:120]))
    pp("".join(l[120:160]))
    pp("".join(l[160:200]))
    pp("".join(l[200:240]))

    # visual inspection
    return "FECZELHE"


submit(2, part2(lines), force=False)
