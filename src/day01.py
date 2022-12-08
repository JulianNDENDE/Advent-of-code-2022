#!/usr/bin/env python3

from typing import List
from tools.openExample import openExample


def calculateMaxCalories(ex: List[str], maxCalories: int = 0) -> int:
    tmp = 0
    for line in ex:
        if line != "":
            tmp += int(line)
            if tmp > maxCalories:
                maxCalories = tmp
        else:
            tmp = 0
    return maxCalories

def calculateTopThreeCalories(ex: List[str], first: int = 0, second: int = 0, third: int = 0):
    tmp = 0
    for line in ex:
        if line != "":
            tmp += int(line)
            if tmp > first:
                third = second
                second = first
                first = tmp
            elif tmp > second:
                third = second
                second = tmp
            elif tmp > third:
                third = tmp
        else:
            tmp = 0
    return first + second + third


def main() -> int:
    example01 = openExample("src/examples/ex01.txt")
    print(calculateMaxCalories(example01))
    print(calculateTopThreeCalories(example01))
    return 0

if __name__ == "__main__":
    exit(main())