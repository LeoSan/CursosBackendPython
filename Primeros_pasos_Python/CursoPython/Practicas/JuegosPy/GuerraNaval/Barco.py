class Barco:
    def __init__(self, nombre, tamanio):
        self.nombre = nombre
        self.tamanio = tamanio
        self.posiciones = [] #lista de coordenadas (fila, columnas)
        self.impactos = [False]
    
    def colocar(self, posiciones):
        if len(posiciones) != self.tamanio:
            raise ValueError(f"Se debe proporcionar {self.tamanio} posiciones para el barco {self.posiciones}" )

        self.posiciones = posiciones
    
    def recibir_impacto(self, posicion):
        if posicion in self.posiciones:
            indice = self.posiciones.index(posicion)
            self.impactos[indice] = True 
            return True
        return False
    
    def esta_hundido(self):
        return all(self.impactos)