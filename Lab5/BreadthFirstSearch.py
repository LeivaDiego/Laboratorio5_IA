from typing import List, Tuple

from GraphSearch import GraphSearch
from maze import Maze


class BreadthFirstSearch(GraphSearch):
    def __init__(self, maze: Maze):
        super().__init__(maze)
        self.current = self.start
        self.visited = set()
        self.queue = []

    def solve(self) -> List[List[Tuple[int, int]]]:

        pass

    def _reach_goal(self, goal: Tuple[int, int]) -> List[Tuple[int, int]]:
        neighbors = self._actions(self.current[0], self.current[1])

        for neighbor in neighbors:
            if neighbor not in self.visited:
                self.queue.append(neighbor)
                self.visited.add(neighbor)
                self.current = neighbor


    def _actions(self, x: int, y: int) -> List[Tuple[int, int]]:
        pass

    def get_path(self) -> List[Tuple[int, int]]:
        pass



