"""Puzzle 4"""

import pathlib
from typing import List, Tuple
import numpy as np

TYPE = Tuple[List[int], List[List[List[int]]]]
INPUT_FILE_NAME = 'input.txt'
INPUT_PATH = pathlib.Path(__file__).parent.resolve().joinpath(INPUT_FILE_NAME)

def make_int(arr: List[str]) -> List[int]:
    """ Make a list of strings into ints """
    return [int(x) for x in arr]


def parse_board(board: str) -> List[List[int]]:
    """ Parse a bingo board """
    finished_board = []
    for row in board.splitlines():
        finished_board.append(row.split())
    return [make_int(row) for row in finished_board]


def parse(data: str) -> TYPE:
    """ Parse the entire file """
    data = data.split('\n\n')
    nums, boards = data[0].split(','), data[1:]
    return (make_int(nums), [parse_board(board) for board in boards])


def is_solved(board: List[List[int]]):
    """ See if the board is solved """
    check = [-1, -1, -1, -1, -1]
    for row in board:
        if row == check:
            return True
    board = np.transpose(board).tolist()
    for row in board:
        if row == check:
            return True
    return False


def check_boards(numbers: List[int], board: List[List[int]]) -> int:
    """ See how long it takes for the board to be solved """
    new_board = board
    val = 0
    for k, num in enumerate(numbers):
        for i, row in enumerate(new_board):
            for j, bingo_num in enumerate(row):
                if bingo_num == num:
                    new_board[i][j] = -1
        if is_solved(new_board):
            for row in new_board:
                for number in row:
                    if number != -1:
                        val += number
            return k, val*num
    return -1, -1


def part_one(puzzle_data: TYPE):
    """ Solve part one """
    values = []
    lower = 1000
    for board in puzzle_data[1]:
        values.append(check_boards(puzzle_data[0], board))

    for num, ans in values:
        if num < lower:
            lower = num
            out = ans

    return out


def part_two(puzzle_data):
    """ Solve part two """
    values = []
    upper = 0
    for board in puzzle_data[1]:
        values.append(check_boards(puzzle_data[0], board))

    for num, ans in values:
        if num > upper:
            upper = num
            out = ans

    return out


def solve(puzzle_input):
    """ Solve both parts """
    data = parse(puzzle_input)
    part_one_solution = part_one(data)
    data = parse(puzzle_input)
    part_two_solution = part_two(data)
    print(part_one_solution)
    print(part_two_solution)


if __name__ == "__main__":
    input_file = pathlib.Path(INPUT_PATH).read_text('utf-8').strip()
    solve(input_file)
