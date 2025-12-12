import random # Importamos el módulo random para generar elecciones aleatorias
import matplotlib.pyplot as plt # Importamos la librería para graficar

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
            tuple: (lista_x, lista_y) con la trayectoria completa.
        """
        # Listas para guardar la historia del camino (para graficar)
        trayectoria_x = [0]
        trayectoria_y = [0]
        
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
            
            # Guardamos la posición actual en la historia
            trayectoria_x.append(self.posicion[0])
            trayectoria_y.append(self.posicion[1])

        # Devolvemos las listas con toda la trayectoria
        return trayectoria_x, trayectoria_y

if __name__ == "__main__":
    # Instanciamos (creamos) un nuevo objeto de tipo Borracho
    borrachin = Borracho()
    
    # Definimos cuántos pasos dará
    pasos = 500
    
    # Ejecutamos el método para caminar
    x, y = borrachin.camino_borrachos(pasos=pasos)
    
    # Imprimimos la coordenada final donde terminó
    print(f"Coordenada final: ({x[-1]}, {y[-1]})")
    
    # Calculamos la distancia euclidiana desde el origen (0,0) usando Pitágoras
    distancia_final = (x[-1]**2 + y[-1]**2)**0.5
    print("La distancia final es: ", distancia_final)
    
    # --- CÓDIGO PARA GRAFICAR ---
    plt.figure(figsize=(10, 6)) # Tamaño del gráfico
    plt.plot(x, y, color='blue', alpha=0.6, label='Camino Aleatorio') # Trazamos la línea
    
    # Marcamos el inicio (Verde) y el final (Rojo)
    plt.plot(0, 0, 'go', label='Inicio (0,0)', markersize=10) # 'go' = Green Circle
    plt.plot(x[-1], y[-1], 'rs', label='Fin', markersize=10)  # 'rs' = Red Square
    
    plt.title(f'Camino de Borrachos ({pasos} pasos)')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid(True) # Cuadrícula de fondo
    plt.legend()   # Mostrar leyenda
    plt.show()     # Mostrar ventana con el gráfico