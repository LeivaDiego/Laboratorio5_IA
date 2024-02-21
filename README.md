# Readme GraphSearch - Laboratorio 5 IA

Este programa resuelve laberintos representados como imágenes tipo .bmp utilizando los algoritmos de búsqueda en anchura (BFS), búsqueda en profundidad (DFS) y A* (A estrella). Después de encontrar el camino en el laberinto para cada algoritmo, genera archivos GIF animados que muestran el proceso de búsqueda y la solución encontrada.

## Video Demostrativo
[Video](https://youtu.be/z1LwxTdcVgc)  

## Requisitos
- Python 3.x
- Las siguientes bibliotecas de Python:
  - `numpy`
  - `PIL` (Python Imaging Library)
  - `imageio`
  - `matplotlib`
  - `skimage`
  - `typing`
  - `heapq`

## Uso
1. Asegúrate de tener instalados los requisitos mencionados anteriormente.
2. Clona o descarga este repositorio en tu sistema.
3. Coloca las imágenes de los laberintos en la carpeta "mazes".
4. Ejecuta el archivo main.py.
5. Espera los resultados viendo el progreso en la terminal.
6. Observa los resultados dentro de la carpeta "solutions".

## Detalles del Código
- `main.py` es el punto de entrada del programa. Utiliza los módulos `DepthFirstSearch.py`, `BreadthFirstSearch.py`, `A_star.py` y `maze.py` para realizar las operaciones necesarias.
- `maze.py` contiene la implementación de la clase Maze, que representa la discretización de la imagen.
- `DepthFirstSearch.py`, `BreadthFirstSearch.py` y `A_star.py` contienen las implementaciones de los algoritmos de búsqueda en profundidad, búsqueda en anchura y A* respectivamente.
- El programa recorre cada imagen de laberinto en la carpeta "mazes", resuelve el laberinto utilizando los tres algoritmos y guarda la animación de la solución encontrada en formato GIF en la carpeta raíz del programa.

## Personalización
- Puedes ajustar los parámetros como el tamaño del laberinto, el factor de escala y la velocidad de fotogramas (fps) en el código principal (`main.py`) según tus necesidades.
- Si deseas personalizar aún más el programa, como cambiar las heurísticas utilizadas en el algoritmo A*, puedes modificar el archivo `A_star.py`.

## Algunos de los Resultados
### A* Algorithm with Manhattan Heuristic:
![](https://github.com/LeivaDiego/Laboratorio5_IA/blob/main/Lab5/solutions/maze1_A_Star_man.gif) ![]()
### BFS Algorithm:
![](https://github.com/LeivaDiego/Laboratorio5_IA/blob/main/Lab5/solutions/maze2_BFS.gif)
### DFS Algorithm:
![](https://github.com/LeivaDiego/Laboratorio5_IA/blob/main/Lab5/solutions/maze3_DFS.gif)
### A*Star Algorithm with Euclidean Heuristic:
![](https://github.com/LeivaDiego/Laboratorio5_IA/blob/main/Lab5/solutions/maze4_A_Star_eucl.gif)

