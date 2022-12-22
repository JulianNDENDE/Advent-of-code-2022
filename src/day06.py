#!/usr/bin/env python3

from typing import List
from tools.openExample import openExample

def countFirstStack(ex: str, size: int) -> int:
    for i in range(len(ex)):
        if len(set(ex[i:i + size])) == size:
            return i + size

def main() -> int:
    ex = openExample("src/examples/ex06.txt")

    print(countFirstStack(ex[0], 4))
    print(countFirstStack(ex[0], 14))
    return 0


if __name__ == "__main__":
    exit(main())
