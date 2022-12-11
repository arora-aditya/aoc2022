from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
from math import *
from statistics import *
from helper.submit import *
from utils import *


DAY = 11
setup(DAY)
lines = read_file(DAY)


class Monkey:
    def __init__(self, idx, items, operation, test, true_m, false_m):
        self.idx = idx
        self.items = items
        self.operation = operation[len("new = ") :].strip()
        self.test = int(test[len("divisible by ") :].strip())
        self.true_m = true_m
        self.false_m = false_m
        self.inspect = 0

    def inspected(self):
        self.inspect += 1

    def __str__(self):
        return f"Monkey {self.idx} with items {self.items}\noperation: {self.operation}\ntest: {self.test}\ntrue: {self.true_m}\nfalse: {self.false_m}\nInspectd: {self.inspect} times inspected\n"


# Part 1
##################################################
def part1(lines: List[str]) -> int:
    monkeys = []
    for i in range(0, len(lines), 7):
        monkeys.append(
            Monkey(
                idx=int(lines[i].split(" ")[1][:-2]),
                items=list(
                    map(
                        int,
                        list(lines[i + 1][len("  Starting items: ") :].split(", ")[:]),
                    )
                ),
                operation=lines[i + 2][len("  Operation: ") :].strip(),
                test=lines[i + 3][len("  Test: ") :].strip(),
                true_m=int(
                    lines[i + 4][len("    If true: throw to monkey ") :].strip()
                ),
                false_m=int(
                    lines[i + 5][len("    If false: throw to monkey ") :].strip()
                ),
            )
        )
        print(monkeys[-1])

    for rd in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                old = item
                worry = eval(monkey.operation, locals())
                worry //= 3
                print(item, monkey.operation, worry)
                print(monkey.test)
                monkey.inspected()
                if worry % monkey.test == 0:
                    print("item given to monkey", monkey.true_m)
                    monkeys[monkey.true_m].items.append(worry)
                else:
                    print("item given to monkey", monkey.false_m)
                    monkeys[monkey.false_m].items.append(worry)
            monkey.items = []

    for monkey in monkeys:
        print(monkey)

    so = list(sorted(monkeys, key=lambda x: x.inspect, reverse=True))
    return so[0].inspect * so[1].inspect


submit(1, part1(lines), force=False)


# Part 2
##################################################
def part2(lines: List[str]) -> int:
    # Product of monkeys divisibility checks
    # avoids keeping track of the massive numbers
    BIGG = 19 * 7 * 17 * 13 * 11 * 2 * 5 * 3
    monkeys = []
    for i in range(0, len(lines), 7):
        monkeys.append(
            Monkey(
                idx=int(lines[i].split(" ")[1][:-2]),
                items=list(
                    map(
                        int,
                        list(lines[i + 1][len("  Starting items: ") :].split(", ")[:]),
                    )
                ),
                operation=lines[i + 2][len("  Operation: ") :].strip(),
                test=lines[i + 3][len("  Test: ") :].strip(),
                true_m=int(
                    lines[i + 4][len("    If true: throw to monkey ") :].strip()
                ),
                false_m=int(
                    lines[i + 5][len("    If false: throw to monkey ") :].strip()
                ),
            )
        )

    for rd in range(10_000):
        for monkey in monkeys:
            for item in monkey.items:
                old = item
                worry = eval(monkey.operation, locals())
                worry %= BIGG
                monkey.inspected()
                if worry % monkey.test == 0:
                    monkeys[monkey.true_m].items.append(worry)
                else:
                    monkeys[monkey.false_m].items.append(worry)
            monkey.items = []

    so = list(sorted(monkeys, key=lambda x: x.inspect, reverse=True))
    return so[0].inspect * so[1].inspect


submit(2, part2(lines), force=False)
