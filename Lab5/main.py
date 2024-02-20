from maze import Maze
from DepthFirstSearch import DepthFirstSearch
from A_star import AStar
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
    upscale_factors = [40,30,30,5]
    fps_values = [100,50,50,2]
    
    for maze, upscale, fps in zip(mazes, upscale_factors, fps_values):
        print("-"*20,f"{maze.name}","-"*20,"/n")
        print("-"*20,"DFS","-"*20)
        dfs = DepthFirstSearch(maze)
        paths_dfs = dfs.solve()
        print("Animando y Escalando los caminos...")
        maze.animate_paths(paths_dfs, upscale, "DFS", fps)
        print("-"*20,"A*","-"*20)
        a_star =  AStar(maze)
        paths_a = a_star.solve()
        print("Animando y Escalando los caminos...")
        maze.animate_paths(paths_a, upscale, "A_Star", fps)

if __name__ == '__main__':
    main()
