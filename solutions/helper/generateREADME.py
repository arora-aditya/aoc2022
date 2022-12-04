import datetime

import os
import requests

from getInput import get_cookie
from getInput import get_day_from_args
from bs4 import BeautifulSoup

output_path = os.path.abspath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../README.md")
)


YEAR = 2022


def get_titles(day):
    titles = []
    cookies, headers = get_cookies_and_header()
    for d in range(1, day + 1):
        url = f"https://adventofcode.com/2022/day/{d}"
        response = requests.get(url, headers=headers, cookies=cookies)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("h2").text.split(": ")[1][:-4]
        titles.append(title)
    return titles


def get_data():
    titles = get_titles(get_day_from_args())

    cookies, headers = get_cookies_and_header()
    response = requests.get(
        "https://adventofcode.com/2022/leaderboard/self",
        headers=headers,
        cookies=cookies,
    )

    soup = BeautifulSoup(response.text, "html.parser")
    x = repr(soup.find("pre")).split("\n")[2:-1]
    data = {}
    for i, line in enumerate(x):
        dat = [k for k in line.split(" ") if k != ""]
        day = int(dat[0])
        rank_part1 = int(dat[2])
        rank_part2 = int(dat[5])
        data[f"{day:02}"] = {
            "name": titles[day - 1],
            "part1": rank_part1,
            "part2": rank_part2,
        }
    return data


def get_cookies_and_header():
    cookies = {
        "session": get_cookie(),
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
        "Referer": "https://adventofcode.com/2022/leaderboard",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
        "TE": "trailers",
    }

    return cookies, headers


if __name__ == "__main__":
    headers = [
        f"# Advent of Code {YEAR}",
        "",
        "My solutions to this year's problems linked [here](https://adventofcode.com/2022)",
        "",
        "## Progress",
        "",
    ]

    datastore = get_data()
    max_len_c1, max_len_c2, max_len_c3, max_len_c4 = 3, 0, 0, 0
    for day, info in datastore.items():
        name, rank1, rank2 = info["name"], str(info["part1"]), str(info["part2"])
        name = f"[{name}](https://adventofcode.com/{YEAR}/day/{int(day)})"
        max_len_c1 = max(max_len_c1, len(day))
        max_len_c2 = max(max_len_c2, len(name))
        max_len_c3 = max(max_len_c3, len(rank1))
        max_len_c4 = max(max_len_c4, len(rank2))

    max_len_c2 += 5
    max_len_c3 += 4
    max_len_c4 += 4

    table = [
        ["Day", "Problem", "Part One", "Part Two"],
        [
            ":" + "-" * (x - 2) + ":"
            for x in [max_len_c1, max_len_c2, max_len_c3, max_len_c4]
        ],
    ]

    for day, info in datastore.items():
        day = day
        name = info["name"]
        name = f"[{name}](https://adventofcode.com/{YEAR}/day/{int(day)})"
        rank1 = str(info["part1"])
        rank2 = str(info["part2"])
        if rank1 == "-1" or rank2 == "-1":
            rank1 = " "
            rank2 = " "
        table.append([day, name, rank1, rank2])

    with open(output_path, "w") as f:
        for header in headers:
            f.write(header + "\n")
        for row in table[0:2] + sorted(table[2:]):
            row = " | ".join(
                [
                    row[0].ljust(max_len_c1, " "),
                    row[1].ljust(max_len_c2, " "),
                    row[2].ljust(max_len_c3, " "),
                    row[3].ljust(max_len_c4, " "),
                    "",
                ]
            )
            f.write(row + "\n")
        f.write(f"\n\nAuto-Generated at {datetime.datetime.now()}")
