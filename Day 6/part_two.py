""" Solve part two """

from typing import List

def input_numbers(number_list: List[int]) -> List[int]:
    """ Put the fish cycles into their spaces in the list """
    output_list = [0] * 9
    for num in number_list:
        output_list[num] += 1

    return output_list


def solve_part_two(puzzle_input: List[int]) -> int:
    """ Solve the second part of the question """
    number_key = input_numbers(puzzle_input)
    for _ in range(256):
        duplicates = number_key[0]
        number_key = number_key[1:]
        number_key[6] += duplicates
        number_key.append(duplicates)

    return sum(number_key)
