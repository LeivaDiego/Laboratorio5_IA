from DepthFirstSearch import DepthFirstSearch
from BreadthFirstSearch import BreadthFirstSearch
from A_star import AStar
from maze import Maze
import os

def main():
	mazes_folder_path = "mazes"
	new_sizes = [20, 25, 31, 200]
	upscale_factors = [40, 30, 30, 5]
	fps_values = [100, 40, 35, 1]

	maze_files = os.listdir(mazes_folder_path)
	maze_count = len(maze_files)
	
	for i, (maze_file, new_size, upscale, fps) in enumerate(zip(maze_files, new_sizes, upscale_factors, fps_values)):
		img_path = os.path.join(mazes_folder_path, maze_file)
		maze = Maze(img_path, new_size)
		print("-" * 40)
		print(f"Procesando: {maze_file}")
		print("Matriz del Laberinto discretizado:")
		print(maze.labyrinth)
		print("\nPosicion de inicio:", maze.start_point)
		print("Posiciones de metas:", maze.end_points)
		print(f"Resolucion Discretizada: {new_size}x{new_size} pixeles")
		print(f"Factor de Escalado: x{upscale}")
		print(f"Duracion de frames: {fps}ms")
		
		print("\n","-" * 17, " BFS ", "-" * 18,"\n")
		bfs = BreadthFirstSearch(maze)
		paths_bfs = bfs.solve()
		print(paths_bfs)
		maze.animate_paths(paths_bfs, upscale, "BFS", fps)

		print("\n","-" * 17, " DFS ", "-" * 18,"\n")
		dfs = DepthFirstSearch(maze)
		paths_dfs = dfs.solve()
		print(paths_dfs)
		maze.animate_paths(paths_dfs, upscale, "DFS", fps)

		print("\n","-" * 18, " A* ", "-" * 18, "\n")
		a_star_eucl = AStar(maze)
		print("Heuristica Euclidiana","-"*15)
		paths_a_eucl = a_star_eucl.solve(a_star_eucl.heuristic_euclidean)
		print(paths_a_eucl)
		maze.animate_paths(paths_a_eucl, upscale, "A_Star_eucl", fps)
		
		print("\nHeuristica Manhattan","-"*15)
		a_star_m = AStar(maze)
		paths_a_man = a_star_m.solve(a_star_m.heuristic_manhattan)
		print(paths_a_man)
		maze.animate_paths(paths_a_man, upscale, "A_Star_man", fps)
		print("-" * 40,"\n"*5)
		
		if i < maze_count - 1:
			option = input("¿Desea continuar con el siguiente laberinto?\n(s para sí, cualquier otra tecla para no): ")
			if option.lower() != 's':
				print("Finalizando el programa.")
				break
			print("\n"*5)

if __name__ == "__main__":
	main()
