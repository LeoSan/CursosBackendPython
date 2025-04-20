def sum_numbers(n):
    # Caso base: si n es 0, la suma es 0
    if n == 0:
        return 0
    # Caso recursivo: n + suma de (n-1)
    else:
        return n + sum_numbers(n - 1)

# Llamada a la función
result = sum_numbers(5)
#print(f"Suma de los primeros 5 números es: {result}")

## Ejemplo factorial 

#En código Python, la función factorial se puede definir recursivamente de la siguiente manera:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#print('el factorial del numero es :', factorial(123))


def suma_digitos_recursiva(numero):
        if numero == 0:
            print(f"Este número debe ser positivo o mayor a cero ->  {numero}")
        elif numero < 10:
            return numero
        else:
             #Obtengo el ultimo numero usando su modulo 
             ultimo_numero = numero%10
             #Obtengo el resto para seguir decomponiendo 
             resto_numero  = numero//10
             #Usamos la base 10 de cada digito para sescomponerlo por cada iteracción de recursividad  
             return ultimo_numero + suma_digitos_recursiva(resto_numero)
            
#print('La suma de números recursivos es:', suma_digitos_recursiva(987))
        
#Ejercicio 3: Imprimir números en cuenta regresiva
#Objetivo: Implementar una función recursiva que imprima los números desde un número dado hasta 1.
#Descripción: Si la función recibe el número 5, debería imprimir: 5, 4, 3, 2, 1.
#Tu tarea: Escribe una función llamada cuenta_regresiva_recursiva(n) que tome un entero positivo n como entrada e imprima los números en cuenta regresiva hasta 1 utilizando la recursividad.
        
def cuenta_regresiva_recursiva(n):
    if n == 0: 
        return n
    else:
        print(n)
        aux = n-1
        return cuenta_regresiva_recursiva(aux)
    
print('La cuenta regresiva')
cuenta_regresiva_recursiva(10)
