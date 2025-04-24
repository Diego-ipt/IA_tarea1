import sys
from laberinto import *
from busquedas import *
from interfaz import *
from utils import *

def main():
    # Leer laberintos desde el archivo
    file_path = "d:\\Universidad\\7mo semestre\\IA\\IA_tarea1\\Ejemplos\\a.txt"
    laberintos = read_labyrinth_file(file_path)

    solucion_encontrada = False
    for laberinto in reversed(laberintos):  # Iterar desde el último laberinto
        arbol = arbol_busqueda(laberinto)
        solucion = dfs(arbol, laberinto.destino)
        if solucion:  # Si se encuentra una solución
            solucion_encontrada = True
            interfaz = Interfaz(laberinto, solucion)
            interfaz.animar_solucion()
            break

    if not solucion_encontrada:
        print("No se encontró solución para ningún laberinto.")

if __name__ == "__main__":
    main()