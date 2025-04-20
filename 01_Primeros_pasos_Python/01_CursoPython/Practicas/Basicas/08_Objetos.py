import random

class Robot:
    def __init__(self, nombre, color, nivel_bateria):
        self.nombre = nombre
        self.color = color
        self.nivel_bateria = nivel_bateria

    def caminar(self):
        if self.nivel_bateria > 10:
            print(f"{self.nombre} está caminando.")
            self.nivel_bateria -= 10  # Reduce la batería al caminar
        else:
            print(f"{self.nombre} necesita recargar batería.")

    def hablar(self, mensaje):
        print(f"{self.nombre} dice: {mensaje}")

    def cargar_bateria(self):
        if self.nivel_bateria > 10:
            print(f"{self.nombre} te informa que mi nivel de bateria aun es suficiente {self.nivel_bateria }.")
        else:  
            self.nivel_bateria = 100
            print(f"{self.nombre} ha recargado su batería al 100%.")

    def dime_algo_inteligente(self):
        mensajes_inteligentes = [
                    "La curiosidad es la brújula que guía el aprendizaje.",
                    "El silencio a menudo contiene respuestas que las palabras no pueden expresar.",
                    "La verdadera sabiduría reside en reconocer lo que aún no sabemos.",
                    "Cada error es una oportunidad disfrazada para crecer.",
                    "El pensamiento crítico es la llave para desbloquear nuevas perspectivas.",
                    "La paciencia es la virtud que convierte los sueños en realidad.",
                    "Adaptarse al cambio es la señal de una mente ágil.",
                    "La empatía es el puente que conecta diferentes corazones.",
                    "La perseverancia es el motor que impulsa el éxito.",
                    "Cuestionar las suposiciones abre la puerta a la innovación."
        ]        
    
        if self.nivel_bateria > 10:
            print(f"{self.nombre} te dice {mensajes_inteligentes[random.randint(0, 10)]}")
            self.nivel_bateria -= 5  # Reduce la batería al caminar
        else:
            print(f"{self.nombre} necesita recargar batería.")



#  Instanciamos la clase y creamos el objeto 
mi_robot = Robot("R2-D2", "blanco", 100)

# Realizamos llamados a los metodos 
mi_robot.caminar()        
mi_robot.hablar("¡Hola!") 

# 
for _ in range(3): 
    mi_robot.caminar()

mi_robot.dime_algo_inteligente()        
mi_robot.cargar_bateria()  
mi_robot.caminar()       