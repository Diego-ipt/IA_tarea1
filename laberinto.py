class Laberinto:
    def __init__(self, filas, columnas, inicio, destino, matriz):
        """
        Inicializa un laberinto con las dimensiones, posiciones inicial y destino, y la matriz de números saltarines.
        """
        self.filas = filas
        self.columnas = columnas
        self.inicio = inicio
        self.destino = destino
        self.matriz = matriz

    def movimientos_validos(self, posicion):
        """
        Calcula los movimientos posibles desde una posición dada según las reglas del laberinto.
        Devuelve un array con las posiciones alcanzables.
        """
        fila, col = posicion
        saltos = self.matriz[fila][col]  # Número saltarín de la celda actual
        movimientos = []
    

        # Abajo
        if fila + saltos < self.filas and (fila + saltos, col) != posicion:
            movimientos.append((fila + saltos, col))
        # Arriba
        if fila - saltos >= 0 and (fila - saltos, col) != posicion:
            movimientos.append((fila - saltos, col))
        # Derecha
        if col + saltos < self.columnas and (fila, col + saltos) != posicion:
            movimientos.append((fila, col + saltos))
        # Izquierda
        if col - saltos >= 0 and (fila, col - saltos) != posicion:
            movimientos.append((fila, col - saltos))
    
        return movimientos

    @classmethod
    def cargar_laberinto_desde_matriz(cls, matriz):
        """
        Carga un único laberinto a partir de una matriz de números proporcionada como entrada.
        La matriz debe incluir las dimensiones, posiciones inicial y destino, y la matriz de números saltarines.
        """
        # Extraer las dimensiones y posiciones inicial/destino de la primera fila
        primera_fila = matriz[0]
        m, n, fila_inicio, col_inicio, fila_destino, col_destino = map(int, primera_fila.split())
    
        # Validar que las dimensiones sean correctas
        if m <= 0 or n <= 0:
            raise ValueError("Las dimensiones del laberinto deben ser positivas.")
    
        # Validar que las posiciones inicial y destino estén dentro de los límites
        if not (0 <= fila_inicio < m and 0 <= col_inicio < n and 0 <= fila_destino < m and 0 <= col_destino < n):
            raise ValueError("Las posiciones inicial y destino están fuera de los límites del laberinto.")
    
        # Leer la matriz del laberinto
        matriz_numeros = []
        for fila in matriz[1:]:
            numeros = list(map(int, fila.split()))
            if len(numeros) != n:
                raise ValueError(f"Cada fila de la matriz debe tener exactamente {n} columnas.")
            matriz_numeros.append(numeros)
    
        # Validar que el número de filas coincida con m
        if len(matriz_numeros) != m:
            raise ValueError(f"El número de filas en la matriz ({len(matriz_numeros)}) no coincide con {m}.")
    
        # Crear y devolver el objeto Laberinto
        return cls(m, n, (fila_inicio, col_inicio), (fila_destino, col_destino), matriz_numeros)