from typing import List

def openExample(filename: str) -> List[str]:
    content = []

    with open(filename, "r") as f:
        for line in f:
            content.append(line.rstrip())
    return content