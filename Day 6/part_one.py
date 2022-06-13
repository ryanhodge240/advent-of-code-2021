""" Solve part one """

from typing import List

def solve_part_one(puzzle_input: List[int], days: int) -> int:
    """ Solve the first part of the question """
    for _ in range(days):
        puzzle_input = [x - 1 for x in puzzle_input]
        for i, _ in enumerate(puzzle_input):
            if puzzle_input[i] == -1:
                puzzle_input[i] = 6
                puzzle_input.append(8)

    return len(puzzle_input)
