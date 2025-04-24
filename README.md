# Laberinto Saltarines

## Descripción del Proyecto

Laberinto Saltarines es una aplicación que permite a los usuarios explorar laberintos saltarines, donde cada celda contiene un número que indica cuántas posiciones se pueden saltar en línea recta. El objetivo es encontrar el camino más corto desde una celda inicial hasta una celda destino utilizando diferentes algoritmos de búsqueda.

## Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos:

- **main.py**: Punto de entrada de la aplicación. Procesa la entrada, crea el laberinto, ejecuta los algoritmos de búsqueda y muestra los resultados en la consola. También inicializa la interfaz gráfica y permite la interacción del usuario.
  
- **laberinto.py**: Contiene la clase `Laberinto`, que representa un laberinto saltarín. Incluye métodos para cargar el laberinto desde un archivo, validar las dimensiones y posiciones, y determinar los movimientos válidos según los números saltarines en cada celda.
  
- **busquedas.py**: Implementa los algoritmos de búsqueda. Incluye una función para la Búsqueda en Profundidad (DFS) que encuentra caminos desde la celda inicial hasta la celda destino evitando ciclos. También implementa la Búsqueda de Costo Uniforme para garantizar encontrar el camino más corto, utilizando una cola de prioridad para gestionar los nodos según su costo acumulado.
  
- **interfaz.py**: Contiene el código para la interfaz gráfica utilizando PyGame. Muestra la cuadrícula del laberinto, resalta la celda inicial y el destino, y permite al usuario interactuar con el laberinto saltando según las reglas. También puede mostrar las soluciones encontradas por los algoritmos DFS y de Costo Uniforme.
  
- **utils.py**: Incluye funciones auxiliares, como la lectura del archivo de entrada, el análisis de los datos del laberinto y la realización de validaciones básicas para asegurar que los datos son coherentes.
  
- **README.md**: Este archivo, que proporciona documentación sobre el proyecto, incluyendo una visión general de la aplicación, instrucciones para ejecutarla y ejemplos de entrada y salida.

- **Informe.pdf**: Documento que proporciona un breve informe describiendo las funciones del código y un ejemplo de entrada/salida que difiere del ejemplo proporcionado.

## Instrucciones para Ejecutar

1. Asegúrate de tener Python instalado en tu sistema.
2. Clona este repositorio o descarga los archivos.
3. Coloca el archivo de texto con los laberintos en la misma carpeta del proyecto.
4. Ejecuta `main.py` desde la línea de comandos:
   ```
   python main.py <nombre_del_archivo_de_laberinto.txt>
   ```
5. Sigue las instrucciones en la consola para interactuar con el laberinto.

## Ejemplo de Entrada

```
4 4 0 0 3 3
2 1 2 1
1 2 1 1
1 1 1 1
1 1 1 0
0
```

## Ejemplo de Salida

```
Número mínimo de movimientos: 4
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un issue o un pull request.