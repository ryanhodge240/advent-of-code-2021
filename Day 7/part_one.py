""" Solve part one """

def solve_part_one(puzzle_input):
    """ Solve the first part of the question """
    best = 1000000
    for i in range(max(puzzle_input)):
        sum_of_distances = 0
        for num in puzzle_input:
            sum_of_distances += abs(num - i)
        if sum_of_distances < best:
            best = sum_of_distances
    return best
