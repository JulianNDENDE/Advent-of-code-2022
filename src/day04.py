#!/usr/bin/env python3

from typing import List
from tools.openExample import openExample

def getNewPair(pair: str) -> List[int]:
    newPair = []
    pair = pair.split("-")
    for i in range(int(pair[0]), int(pair[1]) + 1):
        newPair.append(i)
    return newPair

def itsIn(ex: List[str], part: int) -> int:
    itsIn: int = 0
    assignment = []
    pair1, pair2 = [], []

    for line in ex:
        assignment = line.split(",")
        pair1 = getNewPair(assignment[0])
        pair2 = getNewPair(assignment[1])
        if len(set(pair1).intersection(pair2)) > part:
            itsIn += 1
    return itsIn

def main() -> int:
    ex = openExample("src/examples/ex04.txt")

    print(itsIn(ex, 1))
    print(itsIn(ex, 0))
    return 0

if __name__ == "__main__":
    exit(main())
