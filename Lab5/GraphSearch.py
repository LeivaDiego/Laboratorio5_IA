from typing import List, Tuple
from maze import Maze
from abc import ABC, abstractmethod


class GraphSearch(ABC):
    def __init__(self, maze: Maze):
        self.matrix = maze.labyrinth
        self.start = maze.start_point
        self.end_points = maze.end_points

    @abstractmethod
    def solve(self) -> List[Tuple[int, int]]:
        """
        Solves the maze and returns a list of coordinates representing the solution path.

        This is an abstract method that must be implemented in concrete subclasses.
        """
        raise NotImplementedError("This method must be implemented in a subclass.")

    @abstractmethod
    def _actions(self, x: int, y: int) -> List[Tuple[int, int]]:
        """
        Gets the legal neighbors of the given cell in the maze.

        Args:
            x: The x-coordinate.
            y: The y-coordinate.

        Returns:
            A list of valid neighbor coordinates as tuples (x, y).
        """
        raise NotImplementedError("This method must be implemented in a subclass.")

    @abstractmethod
    def get_path(self) -> List[Tuple[int, int]]:
        """
        Returns the path to the solution
        """
        raise NotImplementedError("This method must be implemented in a subclass.")

    def get_goals(self) -> List[Tuple[int, int]]:
        """
        Returns the goals of the maze
        """
        return self.end_points

    def get_start(self) -> Tuple[int, int]:
        """
        Returns the start of the maze
        """
        return self.start

    def get_matrix(self) -> List[List[int]]:
        """
        Returns the matrix of the maze
        """
        return self.matrix
