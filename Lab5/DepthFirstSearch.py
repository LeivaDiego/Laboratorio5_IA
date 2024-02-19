from typing import List, Tuple
from GraphSearch import GraphSearch
from maze import Maze


class DepthFirstSearch(GraphSearch):
    def __init__(self, maze: Maze):
        super().__init__(maze)
        self.visited = set()
        self.path = []
        self.current = self.start

    def solve(self) -> List[Tuple[int, int]]:
        while self.current != self.end_points[0]:  # TODO: Manejar multiples metas y caso donde no se encuentre solucion
            self.visited.add(self.current)
            self.path.append(self.current)
            neighbors = self._actions(self.current[0], self.current[1])

            if all(neighbor in self.visited for neighbor in neighbors) or not neighbors:
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
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        new_neighbors = []
        for neighbor in neighbors:
            if self.matrix[neighbor[0]][neighbor[1]] == 1:
                new_neighbors.append(neighbor)

        return new_neighbors

    def _backtrack(self):
        self.path.pop()
        self.current = self.path.pop()
