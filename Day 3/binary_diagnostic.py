"""Puzzle 3"""

import pathlib
from typing import List

INPUT_FILE_NAME = 'input.txt'
INPUT_PATH = pathlib.Path(__file__).parent.resolve().joinpath(INPUT_FILE_NAME)

# Solution to part 1
def power_consumption():
    """Find where the sub is going based on directions"""

    with open(INPUT_PATH, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()
        gamma = find_gamma(lines)
        epsilon = [0 if x == 1 else 1 for x in gamma]
        return int(''.join(str(x) for x in gamma), 2) * int(''.join(str(x) for x in epsilon), 2)

# For part 1 as well
def find_gamma(lines: List[str]) -> List[int]:
    """Given an array of binary numbers, find the gamma numebr"""

    zeros = [0] * (len(lines[0]) - 1)
    ones = [0] * (len(lines[0]) - 1)
    out = [0] * (len(lines[0]) - 1)

    for line in lines:
        line = line.strip()
        for i, letter in enumerate(line):
            if letter == '1':
                ones[i] += 1
            else:
                zeros[i] += 1

    for i, _ in enumerate(ones):
        out[i] = 1 if ones[i] > zeros[i] else 0

    return out

# Solution to part 2
def life_support_rating():
    """Find the life support rating of the sub"""

    with open(INPUT_PATH, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()
        co2_lines = lines
        for i, _ in enumerate(lines[0].strip()):
            ones = []
            zeros = []

            for line in lines:
                if line[i] == '1':
                    ones.append(line)
                else:
                    zeros.append(line)

            lines = ones if len(ones) >= len(zeros) else zeros

        oxygen_rating = int(lines[0].strip(), 2)

        lines = co2_lines
        for i, _ in enumerate(lines[0].strip()):
            ones = []
            zeros = []

            for line in lines:
                if line[i] == '1':
                    ones.append(line)
                else:
                    zeros.append(line)

            if len(ones) == 0:
                lines = zeros
            elif len(zeros) == 0:
                lines = ones
            else:
                lines = ones if len(ones) < len(zeros) else zeros

        co2_rating = int(lines[0].strip(), 2)

        return oxygen_rating * co2_rating


if __name__ == "__main__":
    print(life_support_rating())
