from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from statistics import *
from helper.submit import *
from utils import *


DAY = 3
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def part1(lines: List[str]) -> int:
    ans = 0
    for line in lines:
        first_half = set(line[:len(line)//2])
        second_half = set(line[len(line)//2:])
        # assert len(line[:len(line)//2]) == len(line[len(line)//2 + 1:]), f"{line[:len(line)//2]}:{line[len(line)//2:]}"
        union = first_half & second_half
        val = sum(map(lambda x: ord(x) - ord("a") + 1 if str.islower(x) else ord(x) - ord("A") + 27, union))
        ans += val
    return ans
        

submit(1, part1(lines), force=False)


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    ans = 0
    for a, b, c in zip(*[iter(lines)]*3):
        union = set(a) & set(b) & set(c)
        val = sum(map(lambda x: ord(x) - ord("a") + 1 if str.islower(x) else ord(x) - ord("A") + 27, union))
        ans += val
    return ans

submit(2, part2(lines), force=False)


