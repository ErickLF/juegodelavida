import pygame
import sys
import numpy
from tablero import Tablero

class Simulacion:
    """
    Clase para simular el juego de la vida
    """
    def __init__(self, celda, alto_pantalla, ancho_pantalla):
        self.tablero = Tablero(celda,alto_pantalla,ancho_pantalla)
        self.color_celula_viva = (0, 0, 0) # Negro
        self.color_celula_muerta = (255, 255, 255) # Blanco
        self.tablero.estado_inicial()
        self.alto_pantalla = alto_pantalla
        self.ancho_pantalla = ancho_pantalla

    def handle_keys(self):
        """
        Nos ayuda a controlar el juego
        :return:
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def pintar_tablero(self, surface):
        """
        Funcion para visualizar en pantalla los cambios
        :param surface:
        :return:
        """
        for y in range(0, self.tablero.get_alto_tablero()):
            for x in range(0, self.tablero.get_ancho_tablero()):
                if self.tablero.get_valor_celda(y,x) == 0:
                    r = pygame.Rect((x * self.tablero.get_tam_celda(), y * self.tablero.get_tam_celda()), (self.tablero.get_tam_celda(), self.tablero.get_tam_celda()))
                    pygame.draw.rect(surface, self.color_celula_muerta, r)
                else:
                    rr = pygame.Rect((x * self.tablero.get_tam_celda(), y * self.tablero.get_tam_celda()), (self.tablero.get_tam_celda(), self.tablero.get_tam_celda()))
                    pygame.draw.rect(surface, self.color_celula_viva, rr)

    def actualizar_celulas(self):
        """
        Recorremos todo el tablero para actualizar las celulas
        :return:
        """
        for y in range(0, self.tablero.get_alto_tablero()):
            for x in range(0, self.tablero.get_ancho_tablero()):
                self.reglas(x, y)
        # Actualizamos el tablero
        self.tablero.matriz = numpy.copy(self.tablero.get_tablero_sig_turno())
        # Reiniciamos el tablero de actualizacion
        self.tablero.actualizar_tablaro_cambios()

    def reglas(self,x,y):
        """
        Funcion que se encarga de revisar los 8 vecinos adyacentes a una celda
        inclueyndo en diagonal.

        :param x: posicion en x de la matriz
        :param y: posicion en y de la matriz
        :return:
        """
        cont_vecinos = 0

        # Revisamos si tiene arriba de el hay una celula
        if y > 0:
            if self.tablero.get_valor_celda(y-1,x) == 1:
                cont_vecinos +=1
        # Validamos a la izquierda
        if x > 0:
            if self.tablero.get_valor_celda(y,x-1) == 1:
                cont_vecinos +=1
            if y > 0:
                if self.tablero.get_valor_celda(y-1,x-1) == 1:
                    cont_vecinos += 1
            if y < self.tablero.get_alto_tablero()-1:
                if self.tablero.get_valor_celda(y+1,x-1)== 1:
                    cont_vecinos += 1

        if y < self.tablero.get_alto_tablero()-1:
            if self.tablero.get_valor_celda(y+1,x) == 1:
                cont_vecinos +=1

        if x < self.tablero.get_ancho_tablero()-1:
            if self.tablero.get_valor_celda(y,x+1) == 1:
                cont_vecinos +=1
            if y > 0:
                if self.tablero.get_valor_celda(y-1,x+1) == 1:
                    cont_vecinos += 1
            if y < self.tablero.get_alto_tablero()-1:
                if self.tablero.get_valor_celda(y+1,x+1) == 1:
                    cont_vecinos += 1

        if self.tablero.get_valor_celda(y,x) == 0:
            if cont_vecinos == 3:
                # Mandamos a actualizar el tablero del siguiente turno ya que ha nacido una celula
                self.tablero.actaulizar_celda(y,x,1)
        else:
            if cont_vecinos >1 and cont_vecinos <=3:
                # Mandamos a actualizar el tablero del siguiente turno ya que sigue viva la celula
                self.tablero.actaulizar_celda(y, x, 1)
            else:
                # Ha muerto la celula por sobrepoblacion o por soledad
                self.tablero.actaulizar_celda(y, x, 0)

    def run(self):
        """
        Funcion que manda a preparar todo el entorno de la pantalla
        de video juego utilizando pygame para todo lo visual.
        :return:
        """
        pygame.init()

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.ancho_pantalla, self.alto_pantalla), 0, 32)

        surface = pygame.Surface(screen.get_size())
        surface = surface.convert()


        while (True):
            clock.tick(10)
            self.handle_keys()
            self.pintar_tablero(surface)
            screen.blit(surface, (0, 0))
            pygame.display.update()
            self.actualizar_celulas()