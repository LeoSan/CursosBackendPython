def banana():
    # Esta función define una función llamada banana.
    # La función no toma ningún argumento.
    # Metodos Slices 

    fruit = 'Banana'
    # Esta línea asigna la cadena 'Banana' a la variable fruit.

    print(fruit) #Imprime en la Consola : >>>Banana
    # Esta línea imprime el valor de la variable fruit.

    print(fruit[3:]) #Imprime en la Consola : >>>ana
    # Esta línea imprime la subcadena de fruit que comienza en el índice 3 y continúa hasta el final de la cadena.

    print(fruit[2:3]) #Imprime en la Consola : >>>a
    # Esta línea imprime la subcadena de fruit que comienza en el índice 2 y termina en el índice 3.

    print(fruit[:]) #Imprime en la Consola : >>>Banana
    # Esta línea imprime la cadena fruit completa.

    print(fruit[1:-1:2]) #Imprime en la Consola : >>>Ba
    # Esta línea imprime la subcadena de fruit que comienza en el índice 1, omitiendo cada dos caracteres, y termina en el índice -1.

if __name__ == '__main__':
    banana()
    # Esta línea llama a la función banana.