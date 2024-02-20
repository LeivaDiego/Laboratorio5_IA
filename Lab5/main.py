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
    upscale_factors = [30,30,30,10]
    
    for maze, upscale in zip(mazes, upscale_factors):
        dfs = DepthFirstSearch(maze)
        paths = dfs.solve()
        print(paths)
        maze.animate_paths(paths, upscale, "DFS")

    # Ejecutar A*
    # a_star = AStar(mazes[0])
    # actions = a_star._actions(0, 0)
    # path = a_star.solve()
    # print("Camino encontrado por A*:", path)
    # if path:
    #     maze = mazes[2]
    #     for pos in path:
    #        maze.labyrinth[pos[0]][pos[1]] = 2
    #     maze.visualize()

    # Ejecutar DFS
    # dfs = DepthFirstSearch(mazes[0])
    # camino = dfs.solve()
    #
    # print(camino)
    # maze = mazes[0]
    # maze.visualize()
    # maze_matriz = maze.labyrinth
    #
    # for i in range(len(camino)):
    #     maze_matriz[camino[i][0]][camino[i][1]] = 2
    # print(maze_matriz)

if __name__ == '__main__':
    main()
