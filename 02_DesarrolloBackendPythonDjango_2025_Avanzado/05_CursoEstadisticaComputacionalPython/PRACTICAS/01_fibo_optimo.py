import sys 

def fibonachi_memoria(n, memo={}):
    if n == 0 or n == 1:
        return 1
    
    if n in memo:
        return memo[n]
    
    memo[n] = fibonachi_memoria(n-1, memo) + fibonachi_memoria(n-2, memo)
    return memo[n]
    

if __name__ == '__main__':
    
    resp = True
    while resp == True:
        numero = int(input("Ingrese su número que desea calcular fibonachi:"))
        print(f"El resultado Fibo del numero:{numero} es {fibonachi_memoria(numero)}")    
        opcion = input("Desea continuar teclear letra s/n: ")
        if opcion == "n":
            resp = False
