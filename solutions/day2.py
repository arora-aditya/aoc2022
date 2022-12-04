from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from statistics import *
from helper.submit import *
from utils import *


DAY = 2
setup(DAY)
lines = read_file(DAY)

ROCK = 1
PAPER = 2
SCISS = 3

DRAW = 3
WIN = 6


# Part 1
##################################################
def part1(lines: List[str]) -> int:
    score = 0
    for line in lines:
        opp, you = line.split(" ")
        oo, oy = ord(opp) - ord("A") + 1, ord(you) - ord("X") + 1
        score += oy
        if oo == oy:
            score += DRAW
        if opp == "A" and you == "Y":
            score += WIN
        elif opp == "B" and you == "Z":
            score += WIN
        elif opp == "C" and you == "X":
            score += WIN
    return score

submit(1, part1(lines), force=False)


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    score = 0
    for line in lines:
        opp, result = line.split(" ")
        oo = ord(opp) - ord("A") + 1
        if result == "Y":
            score += DRAW
            score += oo 
        elif result == "X":
            score += {
                "A": SCISS,
                "B": ROCK,
                "C": PAPER,
            }[opp]
        elif result == "Z":
            score += {
                "A": PAPER,
                "B": SCISS,
                "C": ROCK,
            }[opp]
            score += WIN
    return score

submit(2, part2(lines), force=False)


