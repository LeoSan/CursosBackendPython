class Tablero:
    def __init__(self, tamanio=10):
        self.tamanio = tamanio
        self.grid = [['~' for _ in range(tamanio)] for _ in range(tamanio)]
        self.barcos = []
        self.disparos_recibidos = set()
    
    def mostrar(self, ocultar_barcos = True):
        for fila_idx, fila in enumerate(self.grid):
            fila_str = f"{chr(ord('A') + fila_idx)} " # Etiquetas de las filas (A, B, C...)
            for col_idx, celda in  enumerate(fila):
                if ocultar_barcos and celda == '0':
                    fila_str += '~ '
                else:
                    fila_str +=f"{celda} "
            print("  " + " ".join(map(str, range(1, self.tamanio + 1)))) 
    
    def colocar_barco(self, barco, posiciones):
        if not all(0 <= f < self.tamanio and 0 <= c < self.tamanio for f, c  in posiciones):
            raise ValueError("Una o más posiciones están fuera del tablero.")
        for f, c in posiciones:
            if self.grid[f][c] == '0':
                raise ValueError("Una o más posiciones ya están ocupadas por otro barco.")
        barco.colocar(posiciones)
        self.barcos.append(barco)
        for f, c in posiciones:
            self.grid[f][c] = '0' # 'O' representa una parte de un barco
        
    def recibir_disparo(self, fila, columna):
        if not (0 <= fila <= self.tamanio and 0 <= columna < self.tamanio):
            return "Fuera del tablero"
        if (fila, columna) in self.disparos_recibidos:
            return "Ya disparaste aquí"
        
        self.disparos_recibidos.add((fila, columna))

        if self.grid[fila][columna] == '0':
            #Busca el barco impactado
            for barco in self.barcos:
                if (fila, columna) in barco.posiciones:
                    barco.recibir_impacto((fila, columna))
                    self.grid[fila][columna] = 'X' # 'X' representa un impacto en un barco
                    if barco.esta_hundido():
                        return f"!Hundidi! {barco.nombre}"
                    return "¡Tocado!"
        else:
            self.grid[fila][columna] = '*' # '*' representa un disparo al agua
            return "!Agua¡"
        
    def todos_barcos_hundidos(self):
        return all(barco.esta_hundido() for barco in self.barcos)