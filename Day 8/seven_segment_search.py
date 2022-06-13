"""Puzzle 8"""

import pathlib
import parse
import part_one
import part_two

INPUT_FILE_NAME = 'input.txt'
INPUT_PATH = pathlib.Path(__file__).parent.resolve().joinpath(INPUT_FILE_NAME)

def solve(puzzle_input: str) -> None:
    """ Solve both parts """
    data = parse.parse(puzzle_input)
    part_one_solution = part_one.solve_part_one(data)
    part_two_solution = part_two.solve_part_two(data)
    print(part_one_solution)
    print(part_two_solution)


if __name__ == "__main__":
    input_file = pathlib.Path(INPUT_PATH).read_text('utf-8').strip()
    solve(input_file)
