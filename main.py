import sys
from laberinto import *
from busquedas import *
from interfaz import *
from utils import *

DEBUG = False  # Variable global para controlar los mensajes de depuración
VER_DFS = False  # Variable global para controlar la visualización de DFS
VER_COSTO_UNIFORME = False  # Variable global para controlar la visualización de búsqueda de costo uniforme
EJEMPLO_ESTANDAR = True  # Variable global para controlar la carga de un laberinto estándar

def main():
    print("Bienvenido al programa de búsqueda de caminos en laberintos.")
    
    # Solicitar al usuario el archivo de laberintos
    if EJEMPLO_ESTANDAR==False:
        file_path = input("Por favor, ingrese la ruta del archivo de laberintos: ").strip()
    else:
        file_path = r"D:\Universidad\7mo semestre\IA\IA_tarea1\Ejemplos\guia.txt"

    # Validar la ruta del archivo
    try:
        laberintos = read_labyrinth_file(file_path)
        print(f"Se han cargado {len(laberintos)} laberintos desde el archivo.")
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo en la ruta especificada: {file_path}")
        return
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    for i, laberinto in enumerate(laberintos, start=1):  # Agregar índice para identificar cada laberinto
        print(f"\nProcesando laberinto {i}...")
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
            print(f"DFS - Número de movimientos: {len(camino_dfs)-1}")
            if VER_DFS:
                interfaz = Interfaz(lab, camino_dfs)
                interfaz.animar_solucion()
        else:
            print("DFS - No hay solución")

        # Realizar búsqueda de costo uniforme
        if DEBUG:
            print("Buscando camino usando búsqueda de costo uniforme...")
        camino_costo_uniforme = costo_uniforme(arbol, lab.destino)
        if camino_costo_uniforme:
            print(f"Costo Uniforme - Número de movimientos: {len(camino_costo_uniforme)-1}")
            if VER_COSTO_UNIFORME:
                interfaz = Interfaz(lab, camino_costo_uniforme)
                interfaz.animar_solucion()
        else:
            print("Costo Uniforme - No hay solución")
        

if __name__ == "__main__":
    main()