
ruta_cuento = "/Users/leonard/CursosBackendPython/Primeros_pasos_Python/CursoPython/Practicas/Basicas/cuento.txt"

#Leer un archivo línea por línea
"""with open(ruta_cuento, 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#Leer todas las líneas en una lista
with open(ruta_cuento, 'r') as file:
    lines = file.readlines()
    print(lines)

#Añadir texto
with open(ruta_cuento, 'a') as file:
    file.write("\n\nBy:Prueba")

#Sobreescribir el texto
#with open(ruta_cuento, 'w') as file:
#    file.write("\n\nBy:Prueba")