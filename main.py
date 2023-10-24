import os
import random
import keyboard
from functools import reduce

class Juego:
    def __init__(self, mapa, inicio, fin):
        self.mapa = mapa
        self.inicio = inicio
        self.fin = fin

    def imprimir_mapa(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for fila in self.mapa:
            print("".join(fila))

    def mover(self, direccion):
        x, y = self.inicio
        nuevo_x, nuevo_y = x, y

        if direccion == "derecha":
            nuevo_y += 1
        elif direccion == "izquierda":
            nuevo_y -= 1
        elif direccion == "arriba":
            nuevo_x -= 1
        elif direccion == "abajo":
            nuevo_x += 1

        if self.es_movimiento_valido(nuevo_x, nuevo_y):
            self.mapa[x][y] = "."  
            self.inicio = (nuevo_x, nuevo_y)
            self.mapa[nuevo_x][nuevo_y] = "P"  
            self.imprimir_mapa()

            if self.inicio == self.fin:
                print("¡Has llegado al destino!")

    def es_movimiento_valido(self, x, y):
        return 0 <= x < len(self.mapa) and 0 <= y < len(self.mapa[0]) and self.mapa[x][y] != "#"

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        self.path_a_mapas = path_a_mapas
        self.elegir_mapa()

    def elegir_mapa(self):
        archivo_mapa = random.choice(os.listdir(self.path_a_mapas))
        mapa, inicio, fin = self.leer_mapa(os.path.join(self.path_a_mapas, archivo_mapa))
        super().__init__(mapa, inicio, fin)

    def leer_mapa(self, path_archivo):
        with open(path_archivo, "r") as archivo:
            lineas = archivo.readlines()

            inicio = self.obtener_coordenadas(lineas[0])
            fin = self.obtener_coordenadas(lineas[1])

            mapa = list(map(list, map(str.strip, reduce(lambda x, y: x + y, lineas[2:], ""))))
            
        return mapa, inicio, fin

    @staticmethod
    def obtener_coordenadas(linea):
        coordenadas = []
        for parte in linea.strip().split():
            try:
                coordenadas.append(int(parte))
            except ValueError:
                pass
        return tuple(coordenadas)

if __name__ == "__main__":
    juego_archivo = JuegoArchivo("maps")
    juego_archivo.inicio = (0, 0)  
    juego_archivo.mapa[0][0] = "P" 
    juego_archivo.imprimir_mapa()

    while juego_archivo.inicio != juego_archivo.fin:
        if keyboard.is_pressed('right'):
            juego_archivo.mover("derecha")
        elif keyboard.is_pressed('left'):
            juego_archivo.mover("izquierda")
        elif keyboard.is_pressed('up'):
            juego_archivo.mover("arriba")
        elif keyboard.is_pressed('down'):
            juego_archivo.mover("abajo")
