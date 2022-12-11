from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from statistics import *
from helper.submit import *
from utils import *


DAY = 8
setup(DAY)
lines = read_file(DAY)


def pg(grid):
    print("\n".join(map(lambda x: "".join(map(str, x)), grid)))


# Part 1
##################################################
def part1(lines: List[str]) -> int:
    grid = []
    left = []
    right = []
    up = []
    down = []
    for line in lines:
        grid.append(list(map(int, line.strip())))
        left.append(list(map(lambda x: 0, line.strip())))
        right.append(list(map(lambda x: 0, line.strip())))
        up.append(list(map(lambda x: 0, line.strip())))
        down.append(list(map(lambda x: 0, line.strip())))

    for rn, row in enumerate(grid):
        current_ma = -1
        for i, h in enumerate(row):
            if h > current_ma:
                current_ma = h
                left[rn][i] = 1

    for rn, row in enumerate(grid):
        current_ma = -1
        for i, h in enumerate(reversed(row)):
            if h > current_ma:
                current_ma = h
                right[rn][-i - 1] = 1

    for cn, col in enumerate([*zip(*grid)]):
        current_ma = -1
        for i, h in enumerate(col):
            if h > current_ma:
                current_ma = h
                up[i][cn] = 1

    for cn, col in enumerate([*zip(*grid)]):
        current_ma = -1
        for i, h in enumerate(reversed(col)):
            if h > current_ma:
                current_ma = h
                down[-i - 1][cn] = 1
    su = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            su += (up[i][j] + down[i][j] + left[i][j] + right[i][j]) > 0

    # pg(left)
    # pg(down)

    return su


submit(1, part1(lines), force=False)


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    grid = []
    left = []
    right = []
    up = []
    down = []
    score = []
    for line in lines:
        grid.append(list(map(int, line.strip())))

    def get(i, j):
        if i < 0 or j < 0:
            return -1
        if i >= len(grid) or j >= len(grid[0]):
            return -1

        return grid[i][j]

    @lru_cache(None)
    def calculate_scenery(i, j):
        v = get(i, j)
        if v < 0:
            return 0, 0, 0, 0
        l = get(i, j - 1)
        r = get(i, j + 1)
        u = get(i - 1, j)
        d = get(i + 1, j)

        if l == -1:
            ll = 0
        else:
            ll = 0
            for jj in range(j - 1, -1, -1):
                if v > get(i, jj):
                    ll += 1
                elif v == get(i, jj):
                    ll += 1
                    break
                else:
                    ll += 1
                    break

        if r == -1:
            rr = 0
        else:
            rr = 0
            for jj in range(j + 1, len(grid[0])):
                if v > get(i, jj):
                    rr += 1
                elif v == get(i, jj):
                    rr += 1
                    break
                else:
                    rr += 1
                    break
        if u == -1:
            uu = 0
        else:
            uu = 0
            for ii in range(i - 1, -1, -1):
                if v > get(ii, j):
                    uu += 1
                elif v == get(ii, j):
                    uu += 1
                    break
                else:
                    uu += 1
                    break
        if d == -1:
            dd = 0
        else:
            dd = 0
            for ii in range(i + 1, len(grid[0])):
                if v > get(ii, j):
                    dd += 1
                elif v == get(ii, j):
                    dd += 1
                    break
                else:
                    dd += 1
                    break

        return ll, rr, uu, dd

    ans = -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            s = calculate_scenery(i, j)
            ans = max(ans, s[0] * s[1] * s[2] * s[3])

    return ans


submit(2, part2(lines), force=False)
