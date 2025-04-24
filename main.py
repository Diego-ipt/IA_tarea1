import sys
from laberinto import *
from busquedas import *
from interfaz import *
from utils import *

DEBUG = False  # Variable global para controlar los mensajes de depuración

def main():
    print("Bienvenido al programa de búsqueda de caminos en laberintos.")
    # Leer laberintos desde el archivo
    file_path = "d:\\Universidad\\7mo semestre\\IA\\IA_tarea1\\Ejemplos\\a.txt"
    laberintos = read_labyrinth_file(file_path)
    print(f"Se han cargado {len(laberintos)} laberintos desde el archivo.")

    for laberinto in laberintos:
        lab = laberinto

        # Generar el árbol de búsqueda
        if DEBUG:
            print("Generando árbol de búsqueda...")
        arbol = arbol_busqueda(lab)

        # Realizar búsqueda en profundidad (DFS)
        if DEBUG:
            print("Buscando camino usando DFS...")
        camino_dfs = dfs(arbol, lab.destino)
        if camino_dfs:
            print(len(camino_dfs)-1) # Número de movimientos
        else:
            print("No hay solución")


if __name__ == "__main__":
    main()