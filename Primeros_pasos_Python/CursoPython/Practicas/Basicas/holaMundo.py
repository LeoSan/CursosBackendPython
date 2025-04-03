import io


## Hola mundo Ejemplos 
print('hola Mundo')
nombre = "Leo"
edad = 37
ciudad = "México"
print("Mi nombre es", nombre, "tengo", edad, "años y vivo en", ciudad)

## Separadores 
print("manzana", "banana", "naranja", sep="-")
print(1, 2, 3, sep=", ")

## Especificar el final de línea (end):
## Por defecto, print() añade un salto de línea (\n) al final de la salida. Puedes cambiar este comportamiento utilizando el parámetro end.

print("Esto se imprime en", end=" ")
print("la misma línea.")

for i in range(5):
    print(i, end=", ")
print("fin")

## Usar cadenas formateadas (f-strings):
## Las f-strings (disponibles desde Python 3.6) son una forma concisa y legible de insertar expresiones dentro de cadenas de texto. Se definen prefijando la cadena con una f o F y colocando las expresiones entre llaves

nombre = "Carlos"
puntuacion = 95
print(f"El estudiante {nombre} obtuvo una puntuación de {puntuacion}.")
print(f"El doble de {puntuacion} es {puntuacion * 2}.")

# Usar el método .format():
# El método .format() también permite formatear cadenas, aunque es un poco más verboso que las f-strings.

nombre = "Laura"
profesion = "ingeniera"
print("Mi nombre es {} y soy {}.".format(nombre, profesion))
print("El número {0} al cuadrado es {1}.".format(5, 5**2)) # Usando índices
print("Nombre: {n}, Edad: {e}".format(n="Pedro", e=25)) # Usando nombres de clave

## combinaciones 

productos = ["manzana", "plátano", "uva"]
print("Lista de productos:", *productos, sep=", ", end=".\n¡Gracias!")