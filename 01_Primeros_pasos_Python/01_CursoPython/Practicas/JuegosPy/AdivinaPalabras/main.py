import time 
from Tablero import Tablero 


def iniciar_juego():
    obj_tablero = Tablero()
    obj_tablero.capturarDatos()
    time.sleep(3) 
    obj_tablero.dibujarPresentacion()
    obj_tablero.logicaJuego()
    
if __name__ == "__main__":
    iniciar_juego()
