from laberinto import *
from collections import *

class Nodo:
    def __init__(self, posicion, valor):
        self.valor = valor # (valor en la matriz)
        self.posicion = posicion # (fila, columna)
        self.hijos = []
        self.nodos_visitados = [] # nodos visitados en la rama

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

def arbol_busqueda(Laberinto):
    """
    Suponemos que los movimientos de la misma rama nunca deberian volver al mismo nodo para evitar ciclos
    """
    raiz = Nodo(Laberinto.inicio, Laberinto.matriz[Laberinto.inicio[0]][Laberinto.inicio[1]])
    arbol_busqueda = raiz
    nodos_nivel_actual = [raiz]
    nodos_nivel_one_step = []

    while True:
        # Si no hay nodos en el nivel actual, se pasa al siguiente nivel
        if not nodos_nivel_actual:
            nodos_nivel_actual = nodos_nivel_one_step
            nodos_nivel_one_step = []
            # Si no hay nodos en el nuevo nivel, se termina la busqueda
            # (esto puede suceder si no hay movimientos validos desde el nivel actual)
            if not nodos_nivel_actual:
                break

        # Se explora el nivel actual
        for i in range(len(nodos_nivel_actual)):
            nodo_actual = nodos_nivel_actual[i]
            # Se obtienen los movimientos validos desde el nodo actual
            movimientos_validos = Laberinto.movimientos_validos(nodo_actual.posicion)
           
            # Se añaden los movimientos validos como hijos del nodo actual
            for movimiento in movimientos_validos:
                if movimiento not in nodo_actual.nodos_visitados:
                    nodo_hijo = Nodo(movimiento, Laberinto.matriz[movimiento[0]][movimiento[1]])
                    nodo_hijo.nodos_visitados = nodo_actual.nodos_visitados + [movimiento]
                    nodo_actual.agregar_hijo(nodo_hijo)
                    nodos_nivel_one_step.append(nodo_hijo)

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


def costo_uniforme(arbol_busqueda):
    """
    Suponemos que los movimientos del laberinto tienen 
    el costo = numero de la posicion desde donde
    se salto (cuantos cuadrados saltamos), ya que sino seria un BFS
    """
    camino = []

    return camino
