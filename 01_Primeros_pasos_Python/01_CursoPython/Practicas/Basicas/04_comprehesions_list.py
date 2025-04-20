import io

squares = [x**2 for x in range(1,11)]
#print("Cuadrados:", squares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) +32 for temp in celsius]
#print(f"Temperatura en F: {fahrenheit}")

#Numeros pares
evens = [x for x in range(1,21) if x%2 ==0]
#print(evens)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

#print(matrix)
#print(transposed)

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

#print(transposed)

#Ejercicio 2: Cuadrados de números impares
#Objetivo: Crear una nueva lista que contenga los cuadrados de los números impares de una lista dada.
#Lista de entrada: numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero = [1,2,3,4,5,6,7,8,9,10]
new_list = [ i**2 for i in numero if i%2 !=0  ]
#print(new_list)


#Ejercicio 3: Extracción de iniciales de nombres
#Objetivo: Crear una nueva lista que contenga las iniciales (en mayúscula) de una lista de nombres completos.
#Lista de entrada: nombres = ["ana pérez", "juan gonzález", "maria rodríguez", "pedro lópez"]

nombres = ["ana pérez", "juan gonzález", "maria rodríguez", "pedro lópez"]
new_name_list = [nom[0].upper() for nom in nombres ]
print(new_name_list)

