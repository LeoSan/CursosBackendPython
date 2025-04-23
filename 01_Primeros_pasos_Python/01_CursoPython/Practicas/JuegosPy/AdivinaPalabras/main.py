import datetime
import time 

class Tablero:
    def __init__(self, nombre = 'Ahorcado', nivel = 'facil'):
        self.list_nivel         = {'facil':10, 'medio':5, 'dificil':3 }
        self.list_categoria     = ['animales','pais','cocina','humano'] 
        self.nombre             = nombre
        self.nivel              = nivel
        self.nombre_jugador     = 'Anonimos'
        self.tiempo_inicio      = datetime.datetime.now()
        self.tiempo_fin         = ''
        self.lista_jugadores    = {} # {'jugador':{'fecha':datetime.datetime.now(), 'tiempo':}} 
        self.categoria          = 'animales'
        self.intentos_fallidos  = 0
        self.palabra_secreta   = ''
        self.palabras_del_juego = {
           'animales':['elefante', 'ballenas', 'perro', 'gato', 'caballo'],
           'pais':['mexico', 'colombia', 'venezuela', 'noruega', 'china'],
           'cocina':['pala', 'cuchillo', 'tabla', 'estufa', 'nevera'],
           'humano':['corazon', 'riñon', 'estomago', 'celula', 'cerebro']
        }
        self.vidas = ''
        self.letras_adivinadas = set()

    def capturarDatos(self):
        print("**************************************************************")
        print(f"********* Bienvenido al juego del : {self.nombre} ****************")
        print("**************************************************************")
        print("**************************************************************")
        print("Lee cuidadosamente los pasos para iniciar el juego: ")
        valida = True
        
        while valida:
            try:
                resp_nivel = str(input(f"1. Primero escoge la dificultad  {self.list_nivel}: "))
                self.list_nivel[resp_nivel]
                valida = False
                self.vidas = self.list_nivel[resp_nivel]
            except KeyError as e:
                print(f"Error: Por favor introduce un nivel valido recuerda son estos tres ->{self.list_nivel} ")
        
        print("!Muy Bien! sigamos con el siguiente paso ")       
        nombre_jugador = str(input(f"2. Segundo escoge tu nombre para jugar y guardar tu score: "))
        self.nombre_jugador = nombre_jugador
        print("!Muy Bien! sigamos con el siguiente paso ")  

        valida = True
        while valida:
            try:
                categoria = str(input(f"3. Tercer paso escoge la categoria para adivinar tu palabra {self.list_categoria} "))
                self.palabras_del_juego[categoria]
                valida = False
                self.categoria = categoria
                import random
                random = random.randint(1, 5)
                self.palabra_secreta = self.palabras_del_juego[categoria][random]
            except KeyError as e:
                print(f"Error: Por favor introduce una categoria correcta :  {self.list_categoria} ")
        
    def dibujarAhorcado(self):
        print("**************************************************************************************************************")
        print(f"********* Iniciamos al juego del : {self.nombre}, {self.nombre_jugador } adivina tu palabra ? ****************")
        print(f"********* Dificultad : {self.nivel}                     ****************")
        print(f"********* Vidas      : {self.vidas}                     ****************")
        print(f"********* Categoria  : {self.categoria}                 ****************")
        print(f"********* Tiempo     : {self.tiempo_inicio}             ****************")
        
        dibujo = [
            "  _______  ",
            " |/      |  ",
            " |       ",
            " |       ",
            " |       ",
            " |       ",
            "_|_      "
        ]

        if self.intentos_fallidos >= 1:
            dibujo[2] = " |       O  "
        if self.intentos_fallidos >= 2:
            dibujo[3] = " |       |  "
        if self.intentos_fallidos >= 3:
            dibujo[3] = " |      /|  "
        if self.intentos_fallidos >= 4:
            dibujo[3] = " |      /|\ "
        if self.intentos_fallidos >= 5:
            dibujo[4] = " |      /   "
        if self.intentos_fallidos >= 6:
            dibujo[4] = " |      / \  "

        for linea in dibujo:
            print(linea)

    def capturaLetras(self):
            print("\nPalabra:", " ".join([letra if letra in self.letras_adivinadas else "_" for letra in self.palabra_secreta]))
            letra_ingresada = input("Ingresa una letra: ").upper()
            #print(letra_ingresada)

def iniciar_juego():
    obj_tablero = Tablero()
    obj_tablero.capturarDatos()
    time.sleep(5) 
    obj_tablero.dibujarAhorcado()
    obj_tablero.capturaLetras()

if __name__ == "__main__":
    iniciar_juego()
