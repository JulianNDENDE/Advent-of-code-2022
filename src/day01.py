#!/usr/bin/env python3

from typing import List
from tools.openExample import openExample

"""
For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

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