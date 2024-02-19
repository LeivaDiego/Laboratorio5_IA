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
        # maze.visualize()
        mazes.append(maze)

    return mazes


def main():
    mazes = discretize_maze()
    dfs = DepthFirstSearch(mazes[0])
    camino = dfs.solve()

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
