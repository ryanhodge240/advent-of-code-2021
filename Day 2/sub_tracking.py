"""Puzzle 2"""

import pathlib

INPUT_FILE_NAME = 'input.txt'
INPUT_PATH = pathlib.Path(__file__).parent.resolve().joinpath(INPUT_FILE_NAME)

# Solution to part 1
def track():
    """Find where the sub is going based on directions"""

    horizontal = 0
    depth = 0

    with open(INPUT_PATH, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            words = line.strip().split()
            if words[0] == 'forward':
                horizontal += int(words[1])
            elif words[0] == 'down':
                depth += int(words[1])
            else:
                depth -= int(words[1])

    return depth * horizontal

# Solution to part 2
def track_aim():
    """Find where the sub is going based on directions"""

    horizontal = 0
    depth = 0
    aim = 0

    with open(INPUT_PATH, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            words = line.strip().split()
            if words[0] == 'forward':
                horizontal += int(words[1])
                depth += aim * int(words[1])
            elif words[0] == 'down':
                aim += int(words[1])
            else:
                aim -= int(words[1])

    return depth * horizontal


if __name__ == "__main__":
    print(track())
    print(track_aim())
