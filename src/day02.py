#!/usr/bin/env python3

from typing import List
from tools.openExample import openExample

"""
A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
"""
DICT1: dict = {
        "A": { "X": 3, "Y": 6, "Z": 0 },
        "B": { "X": 0, "Y": 3, "Z": 6 },
        "C": { "X": 6, "Y": 0, "Z": 3 }
    }

VICT1: dict = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

DICT2: dict = {
        "A": { "X": 3, "Y": 1, "Z": 2 },
        "B": { "X": 1, "Y": 2, "Z": 3 },
        "C": { "X": 2, "Y": 3, "Z": 1 }
    }

VICT2: dict = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

def main() -> int:
    res1: int = 0
    res2: int = 0
    example = openExample("src/examples/ex02.txt")

    for line in example:
        line = line.split(" ")
        res1 += (DICT1[line[0]][line[1]] + VICT1[line[1]])
        res2 += (DICT2[line[0]][line[1]] + VICT2[line[1]])

    print(res1)
    print(res2)
    return 0

if __name__ == "__main__":
    exit(main())