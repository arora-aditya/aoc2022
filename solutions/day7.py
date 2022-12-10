from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from parse import *
from pprint import pprint as pp
from math import *
from statistics import *
from helper.submit import *
from utils import *


DAY = 7
setup(DAY)
lines = read_file(DAY)


class Node:
    def __init__(self, path, children):
        self.path = path
        self.children = children
        self.size = None

    def __str__(self):
        c = "\n\t".join(map(str, (self.children)))
        return f"{self.path}, {c}"


def parse_cd_ls(lines):
    path = parse("$ cd {}", lines[0].strip())[0]
    children = []
    for line in lines[2:]:
        result = parse("dir {dir}", line.strip())
        if result is None:
            result = parse("{size:d} {file}", line.strip())
            children.append(("F", result["file"], result["size"]))
        else:
            children.append(("D", result["dir"], 0))

    n = Node(path, children)
    # print(n)
    return n


# Part 1
##################################################
SEP = "#"


def part1(lines: List[str]) -> int:
    nodes = {}
    s = 0
    i = 0
    abs_path = []
    while i < len(lines):
        line = lines[i]
        if line.startswith("$ cd .."):
            i += 1
            abs_path.pop()
            continue
        if line.startswith("$ cd"):
            s = i
            i += 2
            while i < len(lines) and not lines[i].startswith("$"):
                i += 1
            node = parse_cd_ls(lines[s:i])
            abs_path.append(node.path)
            node.path = SEP.join(abs_path)
            nodes[node.path] = node

    def calc_size(path):
        root = nodes[path]
        su = 0
        for child in root.children:
            t, n, s = child
            if t == "F":
                su += s
            elif t == "D":
                su += calc_size(path + SEP + n)
        root.size = su
        return su

    su = 0
    for path, node in nodes.items():
        if calc_size(path) <= 100000:
            su += node.size
    return su


submit(1, part1(lines), force=False)


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    nodes = {}
    s = 0
    i = 0
    abs_path = []
    while i < len(lines):
        line = lines[i]
        if line.startswith("$ cd .."):
            i += 1
            abs_path.pop()
            continue
        if line.startswith("$ cd"):
            s = i
            i += 2
            while i < len(lines) and not lines[i].startswith("$"):
                i += 1
            node = parse_cd_ls(lines[s:i])
            abs_path.append(node.path)
            node.path = SEP.join(abs_path)
            nodes[node.path] = node

    @lru_cache(None)
    def calc_size(path):
        root = nodes[path]
        su = 0
        for child in root.children:
            t, n, s = child
            if t == "F":
                su += s
            elif t == "D":
                su += calc_size(path + SEP + n)
        root.size = su
        return su

    su = 0

    space_needed = 30000000 - (70000000 - calc_size("/"))

    ans = "/"
    mi = float("inf")
    for path, node in nodes.items():
        if calc_size(path) > space_needed:
            if calc_size(path) - space_needed < mi:
                mi = calc_size(path) - space_needed
                ans = calc_size(path)

    return ans


submit(2, part2(lines), force=False)
