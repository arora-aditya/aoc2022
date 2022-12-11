from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from statistics import *
from helper.submit import *
from parse import *
from utils import *


DAY = 9
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def real(k):
    return k.real


def imag(k):
    return k.imag


def sgn(k):
    if k == 0:
        return 0
    return k / abs(k)


def calc_tp(tp, hp, prev_hp, tails):
    if tp == hp:
        return tp
    if abs(real(tp - hp)) == 1 and imag(tp - hp) == 0:
        return tp
    if real(tp - hp) == 0 and abs(imag(tp - hp)) == 1:
        return tp
    if hp == tp + 1 + 1j or hp == tp - 1 - 1j or hp == tp - 1 + 1j or hp == tp + 1 - 1j:
        return tp
    else:
        # import pdb;pdb.set_trace()
        new_tp = tp + sgn(real(hp - tp)) + sgn(imag(hp - tp)) * 1j
        tails.add(new_tp)
        return new_tp


def part1(lines: List[str]) -> int:
    tails = set()
    hp = 0 + 0j
    tp = 0 + 0j
    tails.add(tp)
    for line in lines:
        result = parse("{} {:d}", line.strip())
        di, ct = result[0], result[1]
        if di == "L":
            for i in range(ct):
                prev_hp = hp
                hp -= 1j
                tp = calc_tp(tp, hp, prev_hp, tails)
        elif di == "R":
            for i in range(ct):
                prev_hp = hp
                hp += 1j
                tp = calc_tp(tp, hp, prev_hp, tails)
        elif di == "U":
            for i in range(ct):
                prev_hp = hp
                hp -= 1
                tp = calc_tp(tp, hp, prev_hp, tails)
        elif di == "D":
            for i in range(ct):
                prev_hp = hp
                hp += 1
                tp = calc_tp(tp, hp, prev_hp, tails)

    return len(tails)


submit(1, part1(lines), force=False)


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    tails = set()
    poss = [0 + 0j for i in range(10)]
    tails.add(poss[-1])
    for line in lines:
        result = parse("{} {:d}", line.strip())
        di, ct = result[0], result[1]
        if di == "L":
            for i in range(ct):
                prev_poss = poss[:]
                poss[0] -= 1j
                for i in range(9):
                    poss[1 + i] = calc_tp(
                        poss[1 + i], poss[i], prev_poss[i], tails=set()
                    )
                tails.add(poss[-1])
        elif di == "R":
            for i in range(ct):
                prev_poss = poss[:]
                poss[0] += 1j
                for i in range(9):
                    poss[1 + i] = calc_tp(
                        poss[1 + i], poss[i], prev_poss[i], tails=set()
                    )
                tails.add(poss[-1])
        elif di == "U":
            for i in range(ct):
                prev_poss = poss[:]
                poss[0] -= 1
                for i in range(9):
                    poss[1 + i] = calc_tp(
                        poss[1 + i], poss[i], prev_poss[i], tails=set()
                    )
                tails.add(poss[-1])
        elif di == "D":
            for i in range(ct):
                prev_poss = poss[:]
                poss[0] += 1
                for i in range(9):
                    poss[1 + i] = calc_tp(
                        poss[1 + i], poss[i], prev_poss[i], tails=set()
                    )
                tails.add(poss[-1])
    return len(tails)


submit(2, part2(lines), force=False)
