import time 
from Tablero import Tablero 


def iniciar_juego():
    obj_tablero = Tablero()
    obj_tablero.capturarDatos()
    time.sleep(5) 
    obj_tablero.dibujarAhorcado()
    obj_tablero.capturaLetras()

if __name__ == "__main__":
    iniciar_juego()
