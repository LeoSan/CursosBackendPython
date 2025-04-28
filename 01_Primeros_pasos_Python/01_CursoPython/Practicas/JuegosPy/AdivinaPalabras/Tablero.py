import datetime
import json
import os 
from graficas import grafica_barras 

class Tablero:
    def __init__(self, nombre = 'Ahorcado', nivel = 'facil'):
        self.list_nivel        = {'facil':10, 'medio':5, 'dificil':3 }
        self.list_categoria    = ['animal','pais','cocina','humano'] 
        self.nombre            = nombre
        self.nivel             = nivel
        self.nombre_jugador    = 'Anonimos'
        self.tiempo_inicio     = datetime.datetime.now()
        self.tiempo_fin        = ''
        self.tiempo_score        = ''
        self.lista_jugadores   = {} # {'jugador':{'fecha':datetime.datetime.now(), 'tiempo':}} 
        self.categoria         = 'animal'
        self.palabra_secreta   = ''
        self.is_ganaste        = 0
        self.palabras_del_juego = {
           'animal':['elefante', 'ballenas', 'perro', 'gato', 'caballo'],
           'pais':['mexico', 'colombia', 'venezuela', 'noruega', 'china'],
           'cocina':['pala', 'cuchillo', 'tabla', 'estufa', 'nevera'],
           'humano':['corazon', 'riñon', 'estomago', 'celula', 'cerebro']
        }
        self.vidas = ''
        self.letras_adivinadas = set()
        self.letras_fallidas   = set()
        self.directorio = '/Users/leonard/Documents/Dev/python/CursosBackendPython/01_Primeros_pasos_Python/01_CursoPython/Practicas/JuegosPy/AdivinaPalabras/'

    def mensajeExito(self):
        print("!Muy Bien! sigamos con el siguiente paso \n")

    def capturarDatos(self):
        print("**************************************************************")
        print(f"********* Bienvenido al juego del : {self.nombre} ****************")
        print("**************************************************************")
        print("************************************************************** \n")
        print("Lee cuidadosamente los pasos para iniciar el juego: ")
        valida = True
        
        while valida:
            try:
                resp_nivel = str(input(f"1. Primero escoge la dificultad  {self.list_nivel}: "))
                self.list_nivel[resp_nivel]
                valida = False
                self.vidas = self.list_nivel[resp_nivel]
                self.nivel = resp_nivel
            except KeyError as e:
                print(f"Error: Por favor introduce un nivel valido recuerda son estos tres ->{self.list_nivel} \n")
        self.mensajeExito() 
               
        nombre_jugador = str(input(f"2. Segundo escoge tu nombre para jugar y guardar tu score: "))
        self.nombre_jugador = nombre_jugador
        self.mensajeExito() 

        valida = True
        while valida:
            try:
                categoria = str(input(f"3. Tercer paso escoge la categoria para adivinar tu palabra {self.list_categoria} "))
                self.palabras_del_juego[categoria]
                valida = False
                self.categoria = categoria
                import random
                random = random.randint(0, 4)
                self.palabra_secreta = self.palabras_del_juego[categoria][random]
                self.mensajeExito() 
            except KeyError as e:
                print(f"Error: Por favor introduce una categoria correcta :  {self.list_categoria} \n")
        
    def dibujarPresentacion(self):
        cal_vidas = " ❤️ "*(self.vidas) 
        print("**************************************************************************************************************")
        print(f"********* Iniciamos al juego del : {self.nombre}, {self.nombre_jugador } adivina tu palabra ? ****************")
        print(f"********* Dificultad : {self.nivel}                                ****************")
        print(f"********* Vidas      : {cal_vidas}                     ****************")
        print(f"********* Categoria  : {self.categoria}                            ****************")
        print(f"********* Tiempo     : {self.tiempo_inicio}                        ****************")
                 
    def dibujarPizarra(self):
        pizarra = [
            "  ___    Pizarra     _____ ",
            " |/                     /| ",
            " |                       | ",
            "  ", "  ".join([letra for letra in self.letras_fallidas]) ,
            " |                       | ",
            " |_______________________| ",
            " |                       | ",
            "_|_                     _|_"
        ]

        for linea in pizarra:
            print(linea)

    def dibujarAhorcado(self):
        dibujo = [
            "  _______  ",
            " |/      |  ",
            " |       ",
            " |       ",
            " |       ",
            " |       ",
            "_|_      "
        ]

        if self.nivel == 'facil':
            if self.vidas <= 9:
                dibujo[2] = " |       O   "
            if self.vidas <=8 :
                dibujo[2] = " |      .O  "
            if self.vidas <=7 :
                dibujo[2] = " |      .O.  "  
            if self.vidas <=6 :
                dibujo[3] = " |       | "            
            if self.vidas <= 5:
                dibujo[3] = " |      /|  "
            if self.vidas <= 4:
                dibujo[3] = " |     ./|  "            
            if self.vidas <= 3:
                dibujo[3] = " |     ./|\ "             
            if self.vidas <= 2:
                dibujo[3] = " |     ./|\. "
            if self.vidas <= 1:
                dibujo[4] = " |      /   "
            if self.vidas == 0:
                dibujo[4] = " |      / \  "

        if self.nivel == 'medio':
            if self.vidas <= 4:
                dibujo[2] = " |       O  "
            if self.vidas <= 3:
                dibujo[3] = " |       |  "
            if self.vidas <= 2:
                dibujo[3] = " |      /|  "
            if self.vidas <= 1:
                dibujo[3] = " |      /|\ "
            if self.vidas == 0:
                dibujo[4] = " |      / \  "

        if self.nivel == 'dificil':
            if self.vidas < 2:
                dibujo[2] = " |       O  "
            if self.vidas <= 1:
                dibujo[3] = " |       |  "
            if self.vidas == 0:
                dibujo[3] = " |      /|  "
            if self.vidas <= 2:
                dibujo[3] = " |      /|\ "
            if self.vidas <= 1:
                dibujo[4] = " |      /   "
            if self.vidas == 0:
                dibujo[4] = " |      / \  "

        for linea in dibujo:
            print(linea)

    def validaLetraIngresada(self, letra):        
        if letra in self.palabra_secreta:
            self.letras_adivinadas.add(letra)
            if set(self.palabra_secreta) == self.letras_adivinadas:
                print("\n¡Felicidades!", self.palabra_secreta + "!")
                self.is_ganaste = 1
        else:
            self.letras_fallidas.add(letra)
            self.vidas = self.vidas - 1 
            cal_vidas = " ❤️ "*(self.vidas) 
            if self.vidas > 0:
                print("Letra incorrecta. te quitamos una vida, te quedan :", cal_vidas ) 
                self.dibujarPizarra()

    def logicaJuego(self):
            ## Ingresar validación que solo sea letras 
            while True:
                print("\nPalabra:", " ".join([letra if letra in self.letras_adivinadas else "_" for letra in self.palabra_secreta]))
               # print(self.palabra_secreta)
               # print(self.nivel)

                letra_capturada = input("Ingresa una letra: ").lower()
                self.validaLetraIngresada(letra_capturada)
                self.dibujarAhorcado()

                if self.is_ganaste == 1:#Cuando Gana
                    break 
                
                if self.vidas <=0:#Cuando Pierde 
                    break 
            #Calculo del tiempo 
            self.tiempo_fin     = datetime.datetime.now()
            self.tiempo_score   = self.tiempo_fin - self.tiempo_inicio

            if self.vidas ==0:
                print("\n¡Perdiste! La palabra era:", self.palabra_secreta)
                self.imprimeLoser()
            else:
                print("\Ganaste! Eres afortunado de no perder en este juego!!  ") 
                self.imprimeWin()  
            #Aqui genero el txt con el score 
            score = self.escribeScore()
            #Aqui genero calculo para la grafica
            datos_graficar = self.calculoTotalWinLoser(score)
            #Aqui genero la grafica
            grafica_barras(datos_graficar[0], datos_graficar[1], self.directorio)

    def imprimeWin(self):
        print("..... (¯`v´¯)♥")
        print(".......•.¸.•´")
        print("....¸.•´")
        print("... (")
        print("☻/")
        print("/▌♥♥")
        print("/ \ ♥♥")
        print(f"You win {self.nombre_jugador}")

    def imprimeLoser(self):
        print("..... (¯ ☹ ¯)")
        print(".......•.¸.•´")
        print("....¸.•´")
        print("... (")
        print(" ")
        print("/▌")
        print("/ \ ")
        print(f"You Loser {self.nombre_jugador}")

    def calculoTotalWinLoser(self, score):
        wins = sum(jugador[0]['win'] == 1 for jugador in score)
        losers = len(score) - wins
        resultado = [['win', 'loser'], [wins, losers]]
        return resultado

    def escribeScore(self):
        #Genero Dicionario 
        lista_jugadores = []
        nuevo_registro = [
            {'nombre': self.nombre_jugador, 'fecha':self.tiempo_inicio.isoformat(), 'tiempo':self.tiempo_score.total_seconds(), 'categoria':self.categoria, 'palabra_secreta':self.palabra_secreta, 'nivel':self.nivel, 'win':self.is_ganaste}
        ]

        try:
            # Verifico si el archivo existe
            if os.path.exists(self.directorio + "jugadores.txt"):
                with open(self.directorio + "jugadores.txt", 'r') as file:
                    try:
                        # Cargo el contenido existente como una lista JSON
                        contenido_existente = json.load(file)
                        if isinstance(contenido_existente, list):# Esta es una función incorporada en Python que se utiliza para verificar si un objeto pertenece a una clase específica o a una tupla de clases.
                            lista_jugadores.extend(contenido_existente)
                        else:
                            print("Advertencia: El archivo existente no contiene una lista JSON válida. Se sobrescribirá.")
                    except json.JSONDecodeError:
                        print("Advertencia: Error al decodificar el archivo JSON existente. Se sobrescribirá.")

            # Append para añadir el nuevo registro a la lista
            lista_jugadores.append(nuevo_registro)

            # Escribo la lista actualizada al archivo (sobrescribiendo el contenido anterior)
            with open(self.directorio + "jugadores.txt", 'w') as file:
                json.dump(lista_jugadores, file, indent=4)
            print("Puntaje guardado en jugadores.txt")

        except Exception as e:
            print("Error: ", e)
        return lista_jugadores