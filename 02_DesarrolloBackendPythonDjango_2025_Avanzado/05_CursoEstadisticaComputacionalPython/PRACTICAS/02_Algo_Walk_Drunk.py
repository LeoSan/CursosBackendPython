import random # Importamos el módulo random para generar elecciones aleatorias

class Borracho:
    """Clase que simula el comportamiento de un borracho moviéndose aleatoriamente."""

    def __init__(self):
        # Inicializamos la posición del borracho en las coordenadas [0, 0] (origen)
        # self.posicion es una lista mutable donde el índice 0 es X y el 1 es Y
        self.posicion = [0,0]


    def camino_borrachos(self, pasos=0):
        """
        Simula el movimiento del borracho por una cantidad determinada de pasos.
        Args:
            pasos (int): Número de movimientos que dará el borracho.
        Returns:
            list: La posición final [x, y] después de todos los pasos.
        """
        # (Opcional) Esta elección inicial no se usa, ya que se sobreescribe en el bucle
        direccion = random.choice(["derecha","izquierda","arriba","abajo"])
        
        # Bucle que se ejecuta una vez por cada paso solicitado
        for i in range(pasos):
            # Elegimos aleatoriamente una de las 4 direcciones posibles
            direccion = random.choice(["derecha", "izquierda", "arriba", "abajo"])
            
            # Actualizamos la coordenada X o Y según la dirección elegida
            if direccion == "izquierda":
                self.posicion[0] -= 1 # Restamos 1 a X (movimiento a la izquierda)
            elif direccion == "derecha":
                self.posicion[0] += 1 # Sumamos 1 a X (movimiento a la derecha)
            elif direccion == "arriba":
                self.posicion[1] += 1 # Sumamos 1 a Y (movimiento hacia arriba)
            elif direccion == "abajo":
                self.posicion[1] -= 1 # Restamos 1 a Y (movimiento hacia abajo)
            else:
                return None # Caso de seguridad, por si llega algo inesperado

        # Devolvemos la lista con la posición final [x, y]
        return self.posicion

if __name__ == "__main__":
    # Instanciamos (creamos) un nuevo objeto de tipo Borracho
    borrachin = Borracho()
    
    # Ejecutamos el método para caminar 500 pasos
    direccion_final = borrachin.camino_borrachos(pasos=500)
    
    # Imprimimos la coordenada final donde terminó
    print(direccion_final)
    
    # Calculamos la distancia euclidiana desde el origen (0,0) usando Pitágoras
    # Distancia = raíz_cuadrada(x^2 + y^2)
    distancia_final = (direccion_final[0]**2 + direccion_final[1]**2)**0.5
    
    # Mostramos a cuánta distancia del origen terminó
    print("La distancia final es: ", distancia_final)