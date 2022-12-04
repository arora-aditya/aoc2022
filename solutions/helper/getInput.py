import os
import sys

from dotenv import load_dotenv
from requests import get

YEAR = 2022


def get_cookie():
    load_dotenv()
    return os.getenv("COOKIE")


def download(url: str, file_name: str):
    cookies = {"session": get_cookie()}
    response = get(url, cookies=cookies)
    if not response.content.startswith(b"Please don't"):
        with open(file_name, "wb") as file:
            file.write(response.content)


def create_source_file(d: int):
    with open(f"day{d}.py", "w") as file:
        lines = [
            "from typing import List, Dict, Set\n",
            "from collections import *\n",
            "from functools import lru_cache\n",
            "from pprint import pprint as pp\n",
            "from math import *\n",
            "from statistics import *\n",
            "from helper.submit import *\n",
            "from utils import *\n",
            "\n\n",
            f"DAY = {d}\n",
            "setup(DAY)\n",
            "lines = read_file(DAY)\n",
            "\n\n",
            "# Part 1\n",
            "#" * 50,
            "\ndef part1(lines: List[str]) -> int:",
            '\n    return float("inf")',
            "\n" * 2,
            "submit(1, part1(lines), force=False)\n" "\n\n",
            "# Part 2\n",
            "#" * 50,
            "\ndef part2(lines: List[str]) -> int:",
            '\n    return float("inf")',
            "\n" * 2,
            "submit(2, part2(lines), force=False)\n" "\n\n",
        ]
        file.writelines(lines)


def download_input_for_day(day: int):
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    file_path = f"./inputs/input{day}.txt"
    if os.path.exists(file_path):
        return False
    download(url, file_path)
    return True


def get_day_from_args():
    return int(sys.argv[1])


if __name__ == "__main__":
    day = get_day_from_args()

    if download_input_for_day(day):
        create_source_file(day)
    else:
        print("input already exists")
