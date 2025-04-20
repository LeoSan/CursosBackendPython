import Tablero

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero = Tablero()
        self.flota = []  # Lista de barcos del jugador

    def agregar_barco(self, barco):
        self.flota.append(barco)
    
    def colocar_flota_aleatoriamente(self):
        """Coloca la flota de barcos del jugador de forma aleatoria."""
        import random


        orientaciones = ['horizontal', 'vertical']

        for barco in self.flota:
            colocado = False
            while not colocado:
                orientacion = random.choice(orientaciones)

    def realizar_disparo(self, tablero_enemigo, fila, columna):
        """Realiza un disparo al tablero del enemigo."""
        resultado = tablero_enemigo.recibir_disparo(fila, columna)
        print(f"{self.nombre} dispara a {chr(ord('A') + fila)}{columna + 1}: {resultado}")
        return resultado