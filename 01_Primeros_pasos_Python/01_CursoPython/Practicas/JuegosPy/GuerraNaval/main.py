class Barco:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño
        self.coordenadas = []  # Lista de tuplas (fila, columna) que ocupa el barco
        self.hits = set()      # Conjunto de tuplas (fila, columna) donde el barco ha sido impactado
        self.hundido = False

    def ocupar_casillas(self, coordenadas):
        """Establece las coordenadas que ocupa el barco."""
        if len(coordenadas) == self.tamaño:
            self.coordenadas = coordenadas
        else:
            raise ValueError(f"El número de coordenadas no coincide con el tamaño del barco ({self.tamaño}).")

    def recibir_impacto(self, fila, columna):
        """Registra un impacto en el barco."""
        if (fila, columna) in self.coordenadas:
            self.hits.add((fila, columna))
            if len(self.hits) == self.tamaño:
                self.hundido = True
                print(f"¡Hundiste mi {self.nombre}!")
            return True
        return False

    def esta_hundido(self):
        """Verifica si el barco ha sido hundido."""
        return self.hundido
    
class Tablero:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.grid = [['~' for _ in range(tamaño)] for _ in range(tamaño)] # '~' representa agua, 'O' barco, 'X' impacto, '*' agua impactada
        self.barcos = []

    def mostrar(self, ocultar_barcos=True):
        """Muestra el tablero."""
        print("  " + " ".join(map(str, range(self.tamaño))))
        for i, fila in enumerate(self.grid):
            fila_str = " ".join(fila)
            if ocultar_barcos:
                fila_str = fila_str.replace('O', '~') # Oculta los barcos al mostrar el tablero del oponente
            print(f"{i} {fila_str}")

    def colocar_barco(self, barco, fila_inicio, columna_inicio, orientacion):
        """Coloca un barco en el tablero."""
        coordenadas = []
        if orientacion == 'horizontal':
            if columna_inicio + barco.tamaño > self.tamaño:
                raise ValueError("El barco se sale del tablero.")
            for i in range(barco.tamaño):
                coordenadas.append((fila_inicio, columna_inicio + i))
        elif orientacion == 'vertical':
            if fila_inicio + barco.tamaño > self.tamaño:
                raise ValueError("El barco se sale del tablero.")
            for i in range(barco.tamaño):
                coordenadas.append((fila_inicio + i, columna_inicio))
        else:
            raise ValueError("Orientación inválida. Debe ser 'horizontal' o 'vertical'.")

        # Verificar si las casillas están ocupadas
        for f, c in coordenadas:
            if self.grid[f][c] == 'O':
                raise ValueError("No se puede colocar el barco en casillas ocupadas.")

        barco.ocupar_casillas(coordenadas)
        self.barcos.append(barco)
        for f, c in coordenadas:
            self.grid[f][c] = 'O'

    def recibir_disparo(self, fila, columna):
        """Recibe un disparo en el tablero."""
        if not (0 <= fila < self.tamaño and 0 <= columna < self.tamaño):
            raise ValueError("Coordenadas fuera del tablero.")

        if self.grid[fila][columna] in ('X', '*'):
            print("¡Ya disparaste a esta casilla!")
            return False

        for barco in self.barcos:
            if barco.recibir_impacto(fila, columna):
                self.grid[fila][columna] = 'X' # Marca como impacto
                return True

        self.grid[fila][columna] = '*' # Marca como agua impactada
        return False

    def todos_hundidos(self):
        """Verifica si todos los barcos han sido hundidos."""
        return all(barco.esta_hundido() for barco in self.barcos)
    
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero = Tablero()
        self.tablero_oponente = Tablero() # Tablero para registrar los disparos al oponente

    def colocar_flota(self, barcos):
        """Coloca la flota de barcos del jugador en su tablero."""
        print(f"\n{self.nombre}, es hora de colocar tus barcos.")
        for barco in barcos:
            while True:
                try:
                    self.tablero.mostrar(ocultar_barcos=False)
                    fila = int(input(f"Fila de inicio para {barco.nombre} (tamaño {barco.tamaño}): "))
                    columna = int(input(f"Columna de inicio para {barco.nombre} (tamaño {barco.tamaño}): "))
                    orientacion = input("Orientación (horizontal/vertical): ").lower()
                    self.tablero.colocar_barco(barco, fila, columna, orientacion)
                    break
                except ValueError as e:
                    print(f"Error al colocar el barco: {e}")
                except IndexError:
                    print("Coordenadas fuera del tablero. Inténtalo de nuevo.")

    def realizar_disparo(self, oponente):
        """Permite al jugador realizar un disparo al tablero del oponente."""
        while True:
            try:
                self.tablero_oponente.mostrar()
                fila = int(input(f"{self.nombre}, ingresa la fila para disparar: "))
                columna = int(input(f"{self.nombre}, ingresa la columna para disparar: "))
                if oponente.tablero.recibir_disparo(fila, columna):
                    print("¡Impacto!")
                    self.tablero_oponente.grid[fila][columna] = 'X'
                    if oponente.tablero.todos_hundidos():
                        print(f"¡{self.nombre} ha hundido toda la flota de {oponente.nombre}!")
                        return True # Indica que el juego ha terminado
                else:
                    print("¡Agua!")
                    self.tablero_oponente.grid[fila][columna] = '*'
                break
            except ValueError as e:
                print(f"Error: {e}")
            except IndexError:
                print("Coordenadas fuera del tablero. Inténtalo de nuevo.")
        return False # El juego no ha terminado

    def ha_perdido(self):
        """Verifica si el jugador ha perdido todos sus barcos."""
        return self.tablero.todos_hundidos()

def jugar_guerra_naval():
    print("¡Bienvenido a Guerra Naval!")

    # Definir los barcos para cada jugador
    barcos_jugador1 = [
        Barco("Portaaviones", 5),
        Barco("Acorazado", 4),
        Barco("Destructor", 3),
        Barco("Submarino", 3),
        Barco("Fragata", 2)
    ]
    barcos_jugador2 = [
        Barco("Portaaviones", 5),
        Barco("Acorazado", 4),
        Barco("Destructor", 3),
        Barco("Submarino", 3),
        Barco("Fragata", 2)
    ]

    # Crear los jugadores
    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2")

    # Fase de colocación de barcos
    jugador1.colocar_flota(barcos_jugador1)
    jugador2.colocar_flota(barcos_jugador2)

    # Fase de juego
    jugador_actual = jugador1
    oponente = jugador2

    while True:
        print(f"\nTurno de {jugador_actual.nombre}")
        if jugador_actual.realizar_disparo(oponente):
            break # El juego termina si un jugador hunde toda la flota del otro

        # Cambiar de turno
        jugador_actual, oponente = oponente, jugador_actual

        if jugador1.ha_perdido():
            print(f"\n¡{jugador2.nombre} ha ganado!")
            break
        if jugador2.ha_perdido():
            print(f"\n¡{jugador1.nombre} ha ganado!")
            break
        
if __name__ == "__main__":
    jugar_guerra_naval()