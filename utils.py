from laberinto import Laberinto

"""
EJEMPLO:
5 5 0 0 1 3
3 4 1 3 1
3 3 3 0 2
3 1 2 2 3
4 2 3 3 3
4 1 4 3 2
5 5 0 0 4 4
3 3 2 4 3
2 2 2 1 1
4 3 1 3 4
2 3 1 1 3
1 1 3 2 0
1 30 0 0 0 10
15 11 19 21 7 1 23 12 17 1 0 10 4 9 12 1 10 2 6 10 3 7 4 6 1 3 24 25 23 2
0
"""
def read_labyrinth_file(file_path):
    labyrinths = []
    with open(file_path, 'r') as file:
        while True:
            # Leer la primera línea de especificación del laberinto
            line = file.readline().strip()
            if line == "0":  # Fin del archivo
                break
            if not line:
                continue

            # Parsear dimensiones y posiciones
            m, n, fila_inicio, col_inicio, fila_destino, col_destino = map(int, line.split())
            matriz = []

            # Leer la matriz del laberinto
            for _ in range(m):
                matriz.append(list(map(int, file.readline().strip().split())))

            # Crear el objeto Laberinto
            laberinto = Laberinto.cargar_laberinto_desde_matriz(
                [line] + [" ".join(map(str, row)) for row in matriz]
            )
            labyrinths.append(laberinto)

    return labyrinths
