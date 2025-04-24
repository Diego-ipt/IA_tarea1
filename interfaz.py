import pygame
import sys
import time  # Added for delay in animation

class Interfaz:
    def __init__(self, laberinto, solucion):
        """
        Inicializa la interfaz con el laberinto y su solución.
        """
        self.laberinto = laberinto
        self.solucion = solucion
        self.celda_tamano = 50  # Tamaño de cada celda en píxeles
        self.ancho = laberinto.columnas * self.celda_tamano
        self.alto = laberinto.filas * self.celda_tamano
        self.colores = {
            "fondo": (255, 255, 255),
            "celda": (200, 200, 200),
            "inicio": (0, 255, 0),
            "destino": (255, 0, 0),
            "camino": (0, 0, 255)
        }

    def dibujar_laberinto(self, pantalla):
        """
        Dibuja el laberinto en la pantalla.
        """
        fuente = pygame.font.Font(None, 36)  # Fuente para los números
        for fila in range(self.laberinto.filas):
            for col in range(self.laberinto.columnas):
                color = self.colores["celda"]
                if (fila, col) == self.laberinto.inicio:
                    color = self.colores["inicio"]
                elif (fila, col) == self.laberinto.destino:
                    color = self.colores["destino"]
                pygame.draw.rect(
                    pantalla,
                    color,
                    (col * self.celda_tamano, fila * self.celda_tamano, self.celda_tamano, self.celda_tamano)
                )
                pygame.draw.rect(
                    pantalla,
                    (0, 0, 0),
                    (col * self.celda_tamano, fila * self.celda_tamano, self.celda_tamano, self.celda_tamano),
                    1
                )

                # Dibujar el número correspondiente en la celda
                numero = self.laberinto.matriz[fila][col]
                texto = fuente.render(str(numero), True, (0, 0, 0))
                texto_rect = texto.get_rect(center=(
                    col * self.celda_tamano + self.celda_tamano // 2,
                    fila * self.celda_tamano + self.celda_tamano // 2
                ))
                pantalla.blit(texto, texto_rect)

    def animar_solucion(self):
        """
        Muestra la solución del laberinto como una animación.
        """
        pygame.init()
        pantalla = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Solución del Laberinto")

        for posicion in self.solucion:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pantalla.fill(self.colores["fondo"])
            self.dibujar_laberinto(pantalla)

            # Dibujar el camino recorrido hasta el momento
            for paso in self.solucion[:self.solucion.index(posicion) + 1]:
                fila, col = paso
                pygame.draw.rect(
                    pantalla,
                    self.colores["camino"],
                    (col * self.celda_tamano, fila * self.celda_tamano, self.celda_tamano, self.celda_tamano)
                )
                # Volver a dibujar el número encima del camino
                fuente = pygame.font.Font(None, 36)
                numero = self.laberinto.matriz[fila][col]
                texto = fuente.render(str(numero), True, (0, 0, 0))
                texto_rect = texto.get_rect(center=(
                    col * self.celda_tamano + self.celda_tamano // 2,
                    fila * self.celda_tamano + self.celda_tamano // 2
                ))
                pantalla.blit(texto, texto_rect)

            pygame.display.flip()
            time.sleep(0.5)  # Pausa para la animación

        # Cerrar la ventana automáticamente al finalizar la animación
        pygame.quit()

