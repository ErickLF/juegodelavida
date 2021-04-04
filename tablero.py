import numpy

class Tablero:
    """
    Clase para simular las ceulas del juego en un tablero de
    1 y 0 donde 1 representa a la celula viva y 0 a la celula muerta.
    """
    def __init__(self, tam_celda, alto_pantalla, ancho_pantalla):
        self.tam_celda = tam_celda
        self.alto_tablero = int(alto_pantalla/self.tam_celda)
        self.ancho_tablero = int(ancho_pantalla/self.tam_celda)
        self.matriz = numpy.zeros((self.alto_tablero, self.ancho_tablero))
        self.matriz_sig_turno = numpy.copy(self.matriz)

    def estado_inicial(self):
        """
        Definimos un estado inicial arbitrario para la prueba.
        :return:
        """
        self.matriz[1][1] = 1
        self.matriz[1][2] = 1
        self.matriz[1][3] = 1

        self.matriz[6][1] = 1
        self.matriz[2][2] = 1
        self.matriz[5][3] = 1
        self.matriz[6][2] = 1
        self.matriz[7][2] = 1
        self.matriz[8][3] = 1

    def get_alto_tablero(self):
        return self.alto_tablero

    def get_ancho_tablero(self):
        return self.ancho_tablero

    def get_tam_celda(self):
        return self.tam_celda

    def get_tablero(self):
        return self.matriz

    def get_tablero_sig_turno(self):
        return self.matriz_sig_turno

    def actualizar_tablaro_cambios(self):
        self.matriz_sig_turno = numpy.zeros((self.alto_tablero, self.ancho_tablero))

    def actaulizar_celda(self, posicion_y, posicion_x, valor):
        self.matriz_sig_turno[posicion_y][posicion_x]=valor

    def get_valor_celda(self, posicion_y, posicion_x):
        return self.matriz[posicion_y][posicion_x]