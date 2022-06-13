""" Solve part two """

from typing import List

def solve_part_two(puzzle_input):
    """ Solve the second part of the question """
    return create_graph(puzzle_input)

def create_graph(puzzle_input: List[List[List[int]]]):
    """ Create the graph for the input """
    graph = [[0] * 1000 for x in range(1000)]
    for coordinates in puzzle_input:
        direction = find_direction(coordinates)
        if direction != -1:
            coo_min = min(coordinates[0][~direction], coordinates[1][~direction])
            coo_max = max(coordinates[0][~direction], coordinates[1][~direction])
            const_value = coordinates[0][direction]
            for i in range(coo_min, coo_max + 1):
                if direction == 1:
                    graph[i][const_value] += 1
                else :
                    graph[const_value][i] += 1
        else:
            graph = diagonals(graph, coordinates)

    return count_paths(graph)

def find_direction(coordinate: List[List[int]]):
    """ Find out which way the line is going """
    if coordinate[0][0] == coordinate[1][0]:
        return 0
    if coordinate[0][1] == coordinate[1][1]:
        return 1
    return -1

def count_paths(graph: List[List[int]]) -> int:
    """ Find the number of elements with overlapping lines """
    count = 0
    for row in graph:
        for num in row:
            if num >= 2:
                count += 1
    return count

def diagonals(graph: List[List[int]], coos: List[List[int]]) -> List[List[int]]:
    """ Deal with the diagonal lines """
    # The smaller x-value is always first
    if coos[1][0] < coos[0][0]:
        temp = coos[0]
        coos[0] = coos[1]
        coos[1] = temp

    if coos[0][1] > coos[1][1]:
        multiplier = -1
    else:
        multiplier = 1

    for i in range(abs(coos[0][0] - coos[1][0]) + 1):
        graph[coos[0][0] + i][coos[0][1] + multiplier*i] += 1
    return graph
