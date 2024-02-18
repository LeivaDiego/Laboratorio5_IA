from maze import Maze
import os

def main():
	mazes_folder_path = "mazes"
	new_sizes = [20, 25, 31, 200]
	maze_files = os.listdir(mazes_folder_path)

	for maze_file, new_size in zip(maze_files, new_sizes):
		img_path = os.path.join(mazes_folder_path, maze_file)
		maze = Maze(img_path, new_size)
		print(f"Procesando: {maze_file}")
		print("Matriz del Laberinto discretizada:")
		print(maze.labyrinth)
		print("Posicion de inicio:", maze.start_point)
		print("Posiciones de metas:", maze.end_points)
		print("-" * 40)
		maze.visualize()

if __name__ == '__main__':
	main()
