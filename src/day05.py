#!/usr/bin/env python3

from typing import List
from tools.openExample import openExample

"""
[J]             [F] [M]            
[Z] [F]     [G] [Q] [F]            
[G] [P]     [H] [Z] [S] [Q]        
[V] [W] [Z] [P] [D] [G] [P]        
[T] [D] [S] [Z] [N] [W] [B] [N]    
[D] [M] [R] [J] [J] [P] [V] [P] [J]
[B] [R] [C] [T] [C] [V] [C] [B] [P]
[N] [S] [V] [R] [T] [N] [G] [Z] [W]
 1   2   3   4   5   6   7   8   9 
"""

CRATES: List[List[str]] = [
    ["N", "B", "D", "T", "V", "G", "Z", "J"],
    ["S", "R", "M", "D", "W", "P", "F"],
    ["V", "C", "R", "S", "Z"],
    ["R", "T", "J", "Z", "P", "H", "G"],
    ["T", "C", "J", "N", "D", "Z", "Q", "F"],
    ["N", "V", "P", "W", "G", "S", "F", "M"],
    ["G", "C", "V", "B", "P", "Q"],
    ["Z", "B", "P", "N"],
    ["W", "P", "J"],
]


def moveCratesRec(
    crates: List[List[str]], move: int, from_: int, to_: int
) -> List[List[str]]:
    if move == 0:
        return crates
    else:
        if len(crates[from_]) == 0:
            crates[from_].append(crates[to_].pop())
        else:
            crates[to_].append(crates[from_].pop())
        crates = moveCratesRec(crates, move - 1, from_, to_)
    return crates


def moveCrates(
    crates: List[List[str]], move: int, from_: int, to_: int
) -> List[List[str]]:
    for _ in range(move):
        if len(crates[from_]) == 0:
            if len(crates[to_]) == 0:
                break
            else:
                crates[from_].append(crates[to_].pop())
        else:
            crates[to_].append(crates[from_].pop())
    return crates


def getTopCrates(crates: List[List[str]]) -> List[str]:
    return [row[-1] if len(row) > 0 else " " for row in crates]


def printCrates(crates: List[List[str]]) -> None:
    for i, row in enumerate(crates):
        print(f"{i:2d} {row}")


def executingTasks(ex: List[List[str]], rec: bool) -> List[List[str]]:
    crates: List[List[str]] = CRATES
    for line in ex:
        move, from_, to_ = [int(x) for x in line.split() if x.isdigit()]
        crates = (
            moveCratesRec(crates, move, from_ - 1, to_ - 1)
            if rec
            else moveCrates(crates, move, from_ - 1, to_ - 1)
        )
    return crates


def main() -> int:
    ex = openExample("src/examples/ex05.txt")
    cratesRec = executingTasks(ex[10:], True)
    crates = executingTasks(ex[10:], False)

    printCrates(crates)
    print(
        "================================================================================================================"
    )
    print("".join(getTopCrates(cratesRec)))
    print(
        "================================================================================================================"
    )
    print("".join(getTopCrates(crates)))
    return 0


if __name__ == "__main__":
    exit(main())
