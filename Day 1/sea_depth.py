"""Puzzle 1"""

import pathlib

INPUT_FILE_NAME = 'input.txt'
INPUT_PATH = pathlib.Path(__file__).parent.resolve().joinpath(INPUT_FILE_NAME)

# Solution to part 1
def get_depth_increases():
    """Find how many times the depth increases"""

    prev = 0
    count = 0

    with open(INPUT_PATH, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            if int(line.strip()) > prev:
                count += 1
            prev = int(line)
    return count - 1

# Solution to part 2
def get_window_increases():
    """Find how many times the window sum increases"""

    count = 0

    with open(INPUT_PATH, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

        for i in range(len(lines) - 3):
            prev_window = sum([int(x.strip()) for x in lines[i:i+3]])
            window = sum([int(x.strip()) for x in lines[i+1:i+4]])

            if prev_window < window:
                count += 1
    return count

if __name__ == "__main__":
    print(get_depth_increases())
    print(get_window_increases())
