""" Solve part one """

from typing import List

def solve_part_one(puzzle_input: List[List[List[str]]]) -> int:
    """ Solve the first part of the question """
    count = 0
    letter_list = [2, 3, 4, 7]
    for line in puzzle_input:
        for num in line[1]:
            if len(num) in letter_list:
                count += 1
    return count
