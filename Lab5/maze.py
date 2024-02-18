from skimage import io, transform, color, measure, morphology
import numpy as np
import matplotlib.pyplot as plt

class Maze:
	"""
	Clase que se utiliza para cargar, procesar y visualizar laberintos a partir de imagenes.
	Esta clase maneja la conversion de imagenes a una representacion de laberinto discretizado,
	identificando areas de inicio y fin basadas en colores especificos, y permite la visualizacion
	del laberinto procesado.

	Attributes:
	----------
		img_path : str
			Ruta al archivo de imagen del laberinto.
		new_size :int
			Dimension al cual se redimensionara la imagen, manteniendo un aspecto cuadrado.
		downscaled_maze : ndarray
			Matriz a color del laberinto redimensionado.
		labyrinth : ndarray
			Matriz binaria del laberinto, donde 1 representa paredes y 0 caminos libres.
		start_point : tuple
			Coordenadas (y, x) del punto de inicio en el laberinto.
		end_points : list
			Lista de coordenadas (y, x) que representan los puntos finales del laberinto.
	"""
	
	def __init__(self, img_path, new_size):
		self.img_path = img_path
		self.new_size = new_size
		self.downscaled_maze = self.load_and_rescale()
		self.labyrinth, self.start_point, self.end_points = self.process_maze()


	def load_and_rescale(self):		
		raw_maze = io.imread(self.img_path)[:, :, :3]
		downscaled_maze = transform.resize(raw_maze, (self.new_size, self.new_size), anti_aliasing=False)
		return downscaled_maze


	def find_closest_to_center(self, mask, center):	
		y, x = np.where(mask)
		if len(y) == 0:
			return None
		positions = np.array([y, x]).T
		distances = np.sqrt(((positions - center) ** 2).sum(axis=1))
		closest_position_idx = np.argmin(distances)
		return (y[closest_position_idx], x[closest_position_idx])


	def find_finish_positions(self, mask_green, label_green, center, props_green):
		closest_positions = []
		for prop in props_green:
			specific_region_mask = (label_green == prop.label)
			closest_position = self.find_closest_to_center(specific_region_mask, center)
			if closest_position:
				closest_positions.append(closest_position)
		return closest_positions


	def identify_areas(self):
		hsv_maze = color.rgb2hsv(self.downscaled_maze)
		red_lower1_hsv, red_upper1_hsv = (0, 0.6, 0.6), (0.05, 1, 1)
		red_lower2_hsv, red_upper2_hsv = (0.95, 0.6, 0.6), (1, 1, 1)
		green_lower_hsv, green_upper_hsv = (0.2, 0.4, 0.4), (0.45, 1, 1)

		mask_red = ((hsv_maze[:, :, 0] >= red_lower1_hsv[0]) & (hsv_maze[:, :, 0] <= red_upper1_hsv[0]) & (hsv_maze[:, :, 1] >= red_lower1_hsv[1]) & (hsv_maze[:, :, 2] >= red_lower1_hsv[2])) | ((hsv_maze[:, :, 0] >= red_lower2_hsv[0]) & (hsv_maze[:, :, 0] <= red_upper2_hsv[0]) & (hsv_maze[:, :, 1] >= red_lower2_hsv[1]) & (hsv_maze[:, :, 2] >= red_lower2_hsv[2]))
		mask_green = ((hsv_maze[:, :, 0] >= green_lower_hsv[0]) & (hsv_maze[:, :, 0] <= green_upper_hsv[0]) & (hsv_maze[:, :, 1] >= green_lower_hsv[1]) & (hsv_maze[:, :, 2] >= green_lower_hsv[2]))

		mask_red_clean = morphology.closing(mask_red, morphology.square(3))
		mask_green_clean = morphology.closing(mask_green, morphology.square(3))

		label_red = measure.label(mask_red_clean)
		label_green = measure.label(mask_green_clean)
		props_green = measure.regionprops(label_green)

		center_of_image = (self.downscaled_maze.shape[0] // 2, self.downscaled_maze.shape[1] // 2)

		closest_start_position = self.find_closest_to_center(mask_red, center_of_image)
		closest_goal_positions = self.find_finish_positions(mask_green, label_green, center_of_image, props_green)

		return closest_start_position, closest_goal_positions


	def binarize_maze_matrix(self):
		gray_maze = color.rgb2gray(self.downscaled_maze)
		binary_maze = gray_maze > 0.1
		return binary_maze


	def adjust_maze_matrix(self, binary_maze, start_position, goal_positions):
		maze_matrix = binary_maze.astype(int)
		padded_maze_matrix = np.pad(maze_matrix, pad_width=1, mode='constant', constant_values=0)
		adjusted_start_position = (start_position[0] + 1, start_position[1] + 1)
		adjusted_goal_positions = [(pos[0] + 1, pos[1] + 1) for pos in goal_positions]
		return padded_maze_matrix, adjusted_start_position, adjusted_goal_positions


	def process_maze(self):
		closest_start_position, closest_goal_positions = self.identify_areas()
		binary_maze = self.binarize_maze_matrix()
		padded_maze_matrix, adjusted_start_position, adjusted_goal_positions = self.adjust_maze_matrix(binary_maze, closest_start_position, closest_goal_positions)
		return padded_maze_matrix, adjusted_start_position, adjusted_goal_positions
	

	def visualize(self):
		height, width = self.labyrinth.shape
		color_labyrinth = np.zeros((height, width, 3), dtype=np.uint8)
		color_labyrinth[self.labyrinth == 1] = [255, 255, 255]
		color_labyrinth[self.start_point[0], self.start_point[1]] = [255, 0, 0]
		for goal in self.end_points:
			color_labyrinth[goal[0], goal[1]] = [0, 255, 0]
		plt.figure(figsize=(8, 8))
		plt.imshow(color_labyrinth, interpolation='nearest')
		plt.title("Laberinto Discretizado")
		plt.axis('off')
		plt.show()