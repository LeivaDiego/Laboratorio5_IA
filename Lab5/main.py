from maze import Maze
from DepthFirstSearch import DepthFirstSearch
import os


def discretize_maze():
    mazes_folder_path = "mazes"
    new_sizes = [20, 25, 31, 200]
    maze_files = os.listdir(mazes_folder_path)
    mazes: list[Maze] = []

    for maze_file, new_size in zip(maze_files, new_sizes):
        img_path = os.path.join(mazes_folder_path, maze_file)
        maze = Maze(img_path, new_size)
        print(f"Procesando: {maze_file}")
        print("Matriz del Laberinto discretizada:")
        print(maze.labyrinth)
        print("Posicion de inicio:", maze.start_point)
        print("Posiciones de metas:", maze.end_points)
        print("-" * 40)
        mazes.append(maze)
        
    return mazes


def main():
    mazes = discretize_maze()
    upscale_factors = [30,30,30,10]
    
    for maze, upscale in zip(mazes, upscale_factors):
        dfs = DepthFirstSearch(maze)
        paths = dfs.solve()
        print(paths)
        maze.animate_paths(paths, upscale, "DFS")

if __name__ == '__main__':
    main()
