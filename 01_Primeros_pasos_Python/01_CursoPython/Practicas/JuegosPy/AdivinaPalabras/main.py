import time 
from Tablero import Tablero 


def iniciar_juego():
    obj_tablero = Tablero()
    obj_tablero.capturarDatos()
    time.sleep(4) 
    obj_tablero.dibujarPresentacion()
    obj_tablero.capturaLetras()

if __name__ == "__main__":
    iniciar_juego()
