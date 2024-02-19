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
    def _move(self, x: int, y: int, direction: str) -> Tuple[int, int]:
        """
        Attempts to move to a neighboring cell in the given direction.

        Args:
            x: The current x-coordinate.
            y: The current y-coordinate.
            direction: The direction to move ("up", "down", "left", "right").

        Returns:
            A tuple of new coordinates (new_x, new_y) if the move is possible,
            otherwise returns the original coordinates (x, y).
        """
        raise NotImplementedError("This method must be implemented in a subclass.")

    def is_wall(self, x: int, y: int) -> bool:
        """
        Checks if the given coordinates represent a wall in the maze.

        Args:
            x: The x-coordinate.
            y: The y-coordinate.

        Returns:
            True if it's a wall, False otherwise.
        """
        value = self.get_coordinate_value(x, y)
        if value == 0:
            return False
        elif value == 1:
            return True

    def get_coordinate_value(self, x: int, y: int) -> int:
        """
        Gets the value of the coordinate in the maze.

        Args:
            x: The x-coordinate.
            y: The y-coordinate.

        Returns:
            The value of the coordinate.
        """
        return self.matrix[x][y]

    @abstractmethod
    def get_neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
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
    def _explore(self, frontier: List[Tuple[int, int]], explored: set):
        """
        Explores the maze from the given frontier, updating explored cells.

        This method is used by concrete subclasses to implement different search
        strategies (e.g., adding/removing cells from the frontier based on algorithm).

        Args:
            frontier: A list of cells to explore next.
            explored: A set of already explored cells.

        Returns:
            None (void method to update internal state).
        """
        raise NotImplementedError("This method must be implemented in a subclass.")

    @abstractmethod
    def _backtrack(self):
        """
        Reconstructs the solution path from the end cell to the start.

        This method is used by concrete subclasses to build the solution path
        after reaching the goal.

        Args:
            start: The coordinates of the start cell.
            end: The coordinates of the end (goal) cell.

        Returns:
            A list of coordinates representing the solution path.
        """
        raise NotImplementedError("This method must be implemented in a subclass.")
