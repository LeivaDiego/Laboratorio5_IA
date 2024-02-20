from typing import List, Tuple
from GraphSearch import GraphSearch
from maze import Maze
import heapq

class AStar(GraphSearch):
    def __init__(self, maze: Maze):
        super().__init__(maze)
        self.path = []
        self.frontier = []
        self.cost_so_far = {}
        self.came_from = {}

    def solve(self) -> List[Tuple[int, int]]:
        start = self.start
        goal = self.end_points[0]  # Tomamos solo el primer punto final
        heapq.heappush(self.frontier, (0, start))
        self.cost_so_far[start] = 0

        while self.frontier:
            current_cost, current_node = heapq.heappop(self.frontier)

            if current_node == goal:
                break

            for next_node in self._actions(current_node[0], current_node[1]):
                new_cost = self.cost_so_far[current_node] + 1  # Coste uniforme en este caso

                if next_node not in self.cost_so_far or new_cost < self.cost_so_far[next_node]:
                    self.cost_so_far[next_node] = new_cost
                    priority = new_cost + self.heuristic(goal, next_node)
                    heapq.heappush(self.frontier, (priority, next_node))
                    self.came_from[next_node] = current_node

        self.path = self.reconstruct_path(start, goal)
        return self.path

    def reconstruct_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
        current_node = goal
        path = []

        while current_node != start:
            path.append(current_node)
            current_node = self.came_from[current_node]

        path.append(start)
        path.reverse()
        return path

    def heuristic(self, a: Tuple[int, int], b: Tuple[int, int]) -> float:
        # Heurística de distancia Manhattan
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def _actions(self, x: int, y: int) -> List[Tuple[int, int]]:
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        new_neighbors = []

        for neighbor in neighbors:
            if 0 <= neighbor[0] < len(self.matrix) and 0 <= neighbor[1] < len(self.matrix[0]) and self.matrix[neighbor[0]][neighbor[1]] == 1:
                new_neighbors.append(neighbor)

        return new_neighbors

    def get_path(self) -> List[Tuple[int, int]]:
        return self.path
