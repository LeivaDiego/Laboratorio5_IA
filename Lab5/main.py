from maze import Maze
from DepthFirstSearch import DepthFirstSearch
from A_star import AStar
import os

def main():
	mazes_folder_path = "mazes"
	new_sizes = [20, 25, 31, 200]
	upscale_factors = [40, 30, 30, 5]
	fps_values = [100, 40, 35, 1]

	maze_files = os.listdir(mazes_folder_path)

	for maze_file, new_size, upscale, fps in zip(maze_files, new_sizes, upscale_factors, fps_values):
		img_path = os.path.join(mazes_folder_path, maze_file)
		maze = Maze(img_path, new_size)
		print(f"Procesando: {maze_file}")
		print("Matriz del Laberinto discretizada:")
		print(maze.labyrinth)
		print("Posicion de inicio:", maze.start_point)
		print("Posiciones de metas:", maze.end_points)
		print(f"Resolucion Discretizada: {new_size}x{new_size} pixeles")
		print(f"Factor de Escalado: x{upscale}")
		print(f"Duracion de frames: {fps}ms")
		
		print("\n","-" * 17, " DFS ", "-" * 18,"\n")
		dfs = DepthFirstSearch(maze)
		paths_dfs = dfs.solve()
		print(paths_dfs)
		maze.animate_paths(paths_dfs, upscale, "DFS", fps)

		print("\n","-" * 18, " A* ", "-" * 18, "\n")
		a_star = AStar(maze)
		paths_a = a_star.solve()
		print(paths_a)
		maze.animate_paths(paths_a, upscale, "A_Star", fps)
		print("-" * 40,"\n"*5)

if __name__ == "__main__":
	main()
