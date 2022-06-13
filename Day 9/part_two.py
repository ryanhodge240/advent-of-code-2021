""" Solve part two """

from typing import List, Tuple
import part_one


def solve_part_two(puzzle_input):
    """ Solve the second part of the question """
    puzzle_input = part_one.pad_graph(puzzle_input)
    biggest_basins = [0, 0, 0]
    basins = get_all_basins(puzzle_input)

    return sum(biggest_basins)

# Use stack to navigate basins
def get_all_basins(graph: List[List[int]]) -> List[int]:
    """ Get the size of all the basins """
    visited = [[False for _ in x] for x in graph]
    stack = []
    for i, row in enumerate(graph):
        for j, num in enumerate(row):
            if not visited[i][j] and num != 9:
                visited[i][j] = True
                stack.append(num)
                while stack:
                    direction = check(graph, (i, j), stack[-1], visited)
                    if direction == 'none':
                        stack.pop()
    return 0


def check(graph: List[List[int]], position: Tuple[int], num: int, visited: List[List[int]]):
    down = graph[position[0]][position[1] + 1]
    down_v = visited[position[0]][position[1] + 1]
    up = graph[position[0]][position[1] - 1]
    up_v = visited[position[0]][position[1] - 1]
    left = graph[position[0] - 1][position[1]]
    left_v = visited[position[0] - 1][position[1]]
    right = graph[position[0] + 1][position[1]]
    right_v = visited[position[0] + 1][position[1]]

    if down < num and not down_v:
        return 'down'
    if up < num and not up_v:
        return 'up'
    if left < num and not left_v:
        return 'left'
    if right < num and not right_v:
        return 'right'
    return 'none'

class Grid_Item:
    def __init__(self) -> None:
        
