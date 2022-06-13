""" Solve part two """

def solve_part_two(puzzle_input):
    """ Solve the second part of the question """
    best = 100000000
    for i in range(max(puzzle_input)):
        sum_of_distances = 0
        for num in puzzle_input:
            sum_of_distances += abs(num - i)*(abs(num - i) + 1)//2
        if sum_of_distances < best:
            best = sum_of_distances
    return best
