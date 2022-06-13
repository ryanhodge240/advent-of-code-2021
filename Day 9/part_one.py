""" Solve part one """

from typing import List, Tuple

def solve_part_one(puzzle_input):
    """ Solve the first part of the question """
    risk = 0
    puzzle_input = pad_graph(puzzle_input)
    for i, row in enumerate(puzzle_input):
        for j, num in enumerate(row):
            if num != 9 and check_depth(puzzle_input, (i, j), num):
                risk += num + 1
    return risk

def pad_graph(graph: List[List[int]]):
    """ Pads the graph with 9's for the edges an corners """
    temp_graph = [9] * (len(graph) + 2)
    for i in range(len(graph) + 2):
        temp_graph[i] = [9] * (len(graph) + 2)
    for i, row in enumerate(graph):
        for j, num in enumerate(row):
            temp_graph[i + 1][j + 1] = num
    return temp_graph

def check_depth(graph: List[List[int]], position: Tuple, value: int):
    """ Check if the value is a low point at its position """
    if graph[position[0] + 1][position[1]] <= value:
        return False
    if graph[position[0] - 1][position[1]] <= value:
        return False
    if graph[position[0]][position[1] + 1] <= value:
        return False
    if graph[position[0]][position[1] - 1] <= value:
        return False
    return True
