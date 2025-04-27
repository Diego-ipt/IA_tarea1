# Laberinto Saltarines

## Consideraciones

En la interfaz gráfica, se mostrará automáticamente primero el recorrido obtenido mediante DFS y luego el recorrido utilizando el algoritmo de costo uniforme. El usuario solo deberá proporcionar la ruta del laberinto a resolver.

## Descripción del Proyecto

Laberinto Saltarines es una aplicación que permite a los usuarios ver laberintos saltarines, donde cada celda contiene un número que indica cuántas posiciones se pueden saltar en línea recta. El objetivo es encontrar el camino más corto desde una celda inicial hasta una celda destino utilizando diferentes algoritmos de búsqueda.

## Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos:

- **main.py**: Punto de entrada de la aplicación. Procesa la entrada, crea el laberinto, ejecuta los algoritmos de búsqueda y muestra los resultados en la consola. También inicializa la interfaz gráfica y permite la interacción del usuario.
  
- **laberinto.py**: Contiene la clase `Laberinto`, que representa un laberinto saltarín. Incluye métodos para cargar el laberinto desde un archivo, validar las dimensiones y posiciones, y determinar los movimientos válidos según los números saltarines en cada celda.
  
- **busquedas.py**: Incluye la creacion de un arbol de desicion para algun laberinto, estos arboles se recorren de manera diferente para implementar costo uniforme y DFS
  
- **interfaz.py**: Contiene el código para la interfaz gráfica utilizando PyGame. Muestra la cuadrícula del laberinto, resalta la celda inicial y el destino. Esta creada para mostrar las soluciones encontradas por los algoritmos DFS y de Costo Uniforme.
  
- **utils.py**: Incluye funciones auxiliares, como la lectura del archivo de entrada.
  
- **README.md**: Este archivo, que proporciona documentación sobre el proyecto, incluyendo una visión general de la aplicación, instrucciones para ejecutarla y ejemplos de entrada y salida.

- **Informe.pdf**: Documento que proporciona un breve informe describiendo las funciones del código y un ejemplo de entrada/salida que difiere del ejemplo proporcionado.

## Instrucciones para Ejecutar

1. Asegúrate de tener Python y pygame instalado en tu sistema.
2. Clona este repositorio o descarga los archivos.
3. Coloca el archivo de texto con los laberintos en la misma carpeta del proyecto.
4. Ejecuta `main.py` desde la línea de comandos:
5. Sigue las instrucciones en la consola para interactuar con el laberinto.

## Ejemplos para probar

\IA_tarea1\Ejemplos\guia.txt
\IA_tarea1\Ejemplos\1.txt
\IA_tarea1\Ejemplos\2.txt
\IA_tarea1\Ejemplos\3.txt

## Ejemplo de Entrada

4 4 0 0 3 3
2 1 1 1
3 3 1 2
3 2 2 1
2 1 3 1
0

## Ejemplo de Salida

Se han cargado 1 laberintos desde el archivo.

Procesando laberinto 1...
DFS - Número de movimientos: 4
Costo Uniforme - Número de movimientos: 3