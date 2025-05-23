from laberinto import *
from collections import *
from heapq import heappush, heappop  # Importar cola de prioridad

DEBUG = False  # Variable global para controlar los mensajes de depuración
DEBUG_2 = False 
class Nodo:
    def __init__(self, posicion, valor):
        self.valor = valor # (valor en la matriz)
        self.posicion = posicion # (fila, columna)
        self.hijos = []
        self.nodos_visitados = [] # nodos visitados en la rama

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

    def __lt__(self, other):
        """
        Define cómo comparar dos nodos. Esto es necesario para usar Nodo en una cola de prioridad.
        En este caso, no importa cómo se comparen porque el costo acumulado se usa como prioridad.
        """
        return False  # Siempre devuelve False porque el costo acumulado es el criterio de comparación

def arbol_busqueda(Laberinto):
    """
    Suponemos que los movimientos de la misma rama nunca deberian volver al mismo nodo para evitar ciclos
    """
    # Crear el nodo raíz a partir de la posición inicial del laberinto
    raiz = Nodo(Laberinto.inicio, Laberinto.matriz[Laberinto.inicio[0]][Laberinto.inicio[1]])
    raiz.nodos_visitados = [Laberinto.inicio]  # Inicializar nodos visitados con la posición inicial
    arbol_busqueda = raiz
    nodos_nivel_actual = [raiz]
    nodos_nivel_one_step = []

    while nodos_nivel_actual:
        # Procesar cada nodo en el nivel actual
        nodo_actual = nodos_nivel_actual.pop(0)  # Usar pop(0) para procesar el primer nodo de la lista
        # Mostrar el nodo actual que se está procesando si DEBUG es True
        if DEBUG:
            print(f"Procesando nodo actual: {nodo_actual.posicion}, valor: {nodo_actual.valor}")

        # Obtener los movimientos válidos desde el nodo actual
        movimientos_validos = Laberinto.movimientos_validos(nodo_actual.posicion)
        # Mostrar los movimientos válidos desde {nodo_actual.posicion} si DEBUG es True
        if DEBUG:
            print(f"Movimientos válidos desde {nodo_actual.posicion}: {movimientos_validos}")

        # Añadir los movimientos válidos como hijos del nodo actual
        for movimiento in movimientos_validos:
            if movimiento not in nodo_actual.nodos_visitados and movimiento != nodo_actual.posicion:
                # Evitar ciclos: no añadir nodos que ya han sido visitados en la misma rama
                # Crear un nuevo nodo hijo
                nodo_hijo = Nodo(movimiento, Laberinto.matriz[movimiento[0]][movimiento[1]])
                if DEBUG:
                    print("nodos_visitados por ",nodo_actual.posicion,": ", nodo_actual.nodos_visitados)
                nodo_hijo.nodos_visitados = nodo_actual.nodos_visitados.copy()
                nodo_hijo.nodos_visitados.append(movimiento)  # Añadir el movimiento actual a la lista de nodos visitados
                if DEBUG:
                    print("nodos_visitados por", nodo_hijo.posicion, ": ",nodo_hijo.nodos_visitados)
                nodo_actual.agregar_hijo(nodo_hijo)
                nodos_nivel_one_step.append(nodo_hijo)
                # Mostrar el nodo hijo que se ha añadido si DEBUG es True
                if DEBUG:
                    print(f"Añadido nodo hijo: {nodo_hijo.posicion}, valor: {nodo_hijo.valor}")

        # Si no hay más nodos en el nivel actual, pasar al siguiente nivel
        if not nodos_nivel_actual:
            nodos_nivel_actual = nodos_nivel_one_step
            nodos_nivel_one_step = []

    # Mostrar que se ha terminado de construir el árbol de búsqueda si DEBUG es True
    if DEBUG_2:
        print("Árbol de búsqueda construido.")

        """
        Imprime el árbol de búsqueda por capas (niveles) de forma clara, mostrando los hijos de cada nodo.
        """
        nivel_actual = [arbol_busqueda]
        nivel = 0

        while nivel_actual:
            print(f"Nivel {nivel}:")
            siguiente_nivel = []
            for nodo in nivel_actual:
                hijos_posiciones = [hijo.posicion for hijo in nodo.hijos]
                print(f"  Nodo {nodo.posicion} -> Hijos: {hijos_posiciones}")
                siguiente_nivel.extend(nodo.hijos)  # Mover esta línea dentro del bucle
            nivel_actual = siguiente_nivel  # Actualizar nivel_actual al final del bucle
            nivel += 1

    return arbol_busqueda


def dfs(arbol_busqueda, destino):
    # el inicio es la raiz del arbol
    """
    Realiza una búsqueda en profundidad (DFS) en el árbol de búsqueda.
    Devuelve el camino desde la raíz hasta el nodo destino si se encuentra.
    """
    stack = [(arbol_busqueda, [arbol_busqueda.posicion])]  # Pila para realizar DFS, contiene nodos y sus caminos

    while stack:
        nodo_actual, camino = stack.pop()  # LIFO 
        if DEBUG_2:
            print(f"stack: {[nodo.posicion for nodo, _ in stack]}")  # Mostrar las posiciones de los nodos en la pila

        # Si encontramos el destino, devolvemos el camino
        if nodo_actual.posicion == destino:
            return camino

        # Agregar los hijos del nodo actual a la pila
        # Si no hay más hijos, el algoritmo retrocede automáticamente al último nodo en la pila (cambio de rama)
        for hijo in nodo_actual.hijos:
            stack.append((hijo, camino + [hijo.posicion]))

    # Si no se encuentra el destino, devolvemos un camino vacío
    return []


def bfs(arbol_busqueda, destino):

    # el inicio es la raiz del arbol
    queue = [(arbol_busqueda, [arbol_busqueda.posicion])]  # Cola para realizar BFS, contiene nodos y sus caminos

    while queue:
        nodo_actual, camino = queue.pop(0)  # Extraer el primer nodo de la cola FIFO

        # Si encontramos el destino, devolvemos el camino
        if nodo_actual.posicion == destino:
            return camino

        # Agregar los hijos del nodo actual a la cola
        for hijo in nodo_actual.hijos:
            queue.append((hijo, camino + [hijo.posicion]))

    # Si no se encuentra el destino, devolvemos un camino vacío
    return []

def costo_uniforme(arbol_busqueda, destino):
    """
    como todos los movimientos tienen el mismo costo, se puede usar BFS para encontrar el camino
    de costo uniforme.
    """
    return bfs(arbol_busqueda, destino)  # Llamar a la función bfs para encontrar el camino de costo uniforme