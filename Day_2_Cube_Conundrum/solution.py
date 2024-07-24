import math
import re


def solution_part_1(games: str) -> int:
    possible = {"red": 12, "green": 13, "blue": 14}
    total = 0
    for idx, game in enumerate(games.split("\n"), start=1):
        for n, color in re.findall(r"(\d+) (red|green|blue)", game):
            if possible[color] < int(n):
                break
        else:
            total += idx

    return total


# with open("puzzles.txt", "r", encoding="utf-8") as f:
#     lines = f.read()
# print(solution_part_1(lines))


# maximun of each color then multiply
def solution_part_2(games: str) -> int:
    total = 0
    for game in games.split("\n"):
        colors = {"red": 0, "green": 0, "blue": 0}
        for n, color in re.findall(r"(\d+) (red|green|blue)", game):
            colors[color] = max(int(n), colors[color])
        total += math.prod(colors.values())
    return total


# with open("puzzles.txt", "r", encoding="utf-8") as f:
#     lines = f.read()
# print(solution_part_2(lines))
