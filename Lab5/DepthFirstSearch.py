from typing import List, Tuple
from GraphSearch import GraphSearch
from maze import Maze


class DepthFirstSearch(GraphSearch):
    def __init__(self, maze: Maze):
        super().__init__(maze)
        self.start = super().start
        self.end_points = super().end_points
        self.visited = set()
        self.path = []
        self.current = self.start

    def solve(self) -> List[Tuple[int, int]]:
        while self.current != self.end_points[0]:  # TODO: Manejar multiples metas y caso donde no se encuentre solucion
            self.visited.add(self.current)
            self.path.append(self.current)
            neighbors = self._actions(self.current[0], self.current[1])

            if all(neighbor in self.visited for neighbor in neighbors):
                self._backtrack()
                continue

            for neighbor in neighbors:
                if neighbor not in self.visited:
                    self.current = neighbor
                    break

        return self.path

    def get_path(self) -> List[Tuple[int, int]]:
        return self.path

    def _actions(self, x: int, y: int) -> List[Tuple[int, int]]:

        pass

    def _explore(self, frontier: List[Tuple[int, int]], explored: set):
        pass

    def _backtrack(self):
        pass
