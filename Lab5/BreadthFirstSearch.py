from typing import List, Tuple

from GraphSearch import GraphSearch
from maze import Maze


class BreadthFirstSearch(GraphSearch):
    def __init__(self, maze: Maze):
        super().__init__(maze)
        self.current = None
        self.visited = set()
        self.queue = [self.start]
        self.parents = {}

    def solve(self) -> List[List[Tuple[int, int]]]:
        paths = []
        print("Aplicando algoritmo BFS...")
        for goal in self.end_points:
            path = self._reach_goal(goal)
            paths.append(path)
        print("Caminos encontrados:")
        return paths

    def _reach_goal(self, goal: Tuple[int, int]) -> List[Tuple[int, int]]:
        to_run = True

        while self.queue and to_run:
            self.current = self.queue.pop(0)

            neighbors = self._actions(self.current[0], self.current[1])
            for neighbor in neighbors:
                if neighbor not in self.visited:
                    self.queue.append(neighbor)
                    self.visited.add(neighbor)
                    self.add_parent(self.current, neighbor)

                    if neighbor == goal:
                        to_run = False
                        break

        return self._backtrack(goal)

    def _backtrack(self, goal: Tuple[int, int]) -> List[Tuple[int, int]]:
        path = []
        if goal in self.parents:
            path.append(goal)
            curr = goal

            while curr != self.start:
                curr = self.parents[curr]
                path.append(curr)

            path.reverse()

        return path

    def add_parent(self, parent: Tuple[int, int], child: Tuple[int, int]):
        self.parents[child] = parent

    def _actions(self, x: int, y: int) -> List[Tuple[int, int]]:
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        new_neighbors = []
        for neighbor in neighbors:
            if self.matrix[neighbor[0]][neighbor[1]] == 1:
                new_neighbors.append(neighbor)

        return new_neighbors

    def get_path(self) -> List[Tuple[int, int]]:
        pass
