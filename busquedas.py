from laberinto import *
from collections import *
from heapq import heappush, heappop  # Importar cola de prioridad

DEBUG = False  # Variable global para controlar los mensajes de depuración

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
            if movimiento not in nodo_actual.nodos_visitados:
                # Crear un nuevo nodo hijo
                nodo_hijo = Nodo(movimiento, Laberinto.matriz[movimiento[0]][movimiento[1]])
                if DEBUG:
                    print("nodos_visitados", nodo_actual.nodos_visitados)
                nodo_hijo.nodos_visitados = nodo_actual.nodos_visitados  # Crear una nueva lista
                nodo_hijo.nodos_visitados.append(movimiento)  # Añadir el movimiento actual a la lista de nodos visitados
                if DEBUG:
                    print("nodos_visitados_new", nodo_hijo.nodos_visitados)
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
    if DEBUG:
        print("Árbol de búsqueda construido.")
    return arbol_busqueda


def dfs(arbol_busqueda, destino):
    # el inicio es la raiz del arbol
    """
    Realiza una búsqueda en profundidad (DFS) en el árbol de búsqueda.
    Devuelve el camino desde la raíz hasta el nodo destino si se encuentra.
    """
    stack = [(arbol_busqueda, [arbol_busqueda.posicion])]  # Pila para realizar DFS, contiene nodos y sus caminos

    while stack:
        nodo_actual, camino = stack.pop()

        # Si encontramos el destino, devolvemos el camino
        if nodo_actual.posicion == destino:
            return camino

        # Agregar los hijos del nodo actual a la pila
        # Si no hay más hijos, el algoritmo retrocede automáticamente al último nodo en la pila (cambio de rama)
        for hijo in nodo_actual.hijos:
            stack.append((hijo, camino + [hijo.posicion]))

    # Si no se encuentra el destino, devolvemos un camino vacío
    return []


def costo_uniforme(arbol_busqueda, destino):
    """
    Realiza una búsqueda de costo uniforme en el árbol de búsqueda.
    Devuelve el camino desde la raíz hasta el nodo destino si se encuentra.
    """
    prioridad = []  # Cola de prioridad para nodos (costo acumulado, nodo, camino)
    heappush(prioridad, (0, arbol_busqueda, [arbol_busqueda.posicion]))

    while prioridad:
        costo_actual, nodo_actual, camino = heappop(prioridad)

        # Si encontramos el destino, devolvemos el camino
        if nodo_actual.posicion == destino:
            return camino

        # Agregar los hijos del nodo actual a la cola de prioridad
        for hijo in nodo_actual.hijos:
            nuevo_costo = costo_actual + hijo.valor
            heappush(prioridad, (nuevo_costo, hijo, camino + [hijo.posicion]))

    # Si no se encuentra el destino, devolvemos un camino vacío
    return []
