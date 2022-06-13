""" Used for creating a Grid object """

from typing import List, Tuple
import part_one

class Grid:
    """ A class for the grid """
    def __init__(self, graph: List[List[int]]) -> None:
        self.width = len(graph)
        self.height = len(graph[0])
        self.graph = part_one.pad_graph(graph)
        self.head = self.init_grid_item(self.graph[0][0], (0, 0))
        self.init_grid()
        pass

    def init_grid(self):
        """ Initialize all the items from the 2D graph """
        current = self.head
        for i, row in enumerate(self.graph):
            for j, num in enumerate(row):
                self.init_grid_item(num, (i, j), current)
                pass

    def init_grid_item(self, value: int, position: Tuple):
        """ Initialize the given value """
        
        pass

class GridItem:
    """ Each item in the grid """
    def __init__(self, value) -> None:
        self.value = value
        self.visited = False

        self.above = None
        self.below = None
        self.left = None
        self.right = None
