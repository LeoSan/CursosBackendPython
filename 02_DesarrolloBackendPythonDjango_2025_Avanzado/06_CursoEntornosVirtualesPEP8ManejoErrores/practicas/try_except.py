"""Ejemplo de manejo de excepciones en Python."""


class DivisionError(Exception):
    """Error en operación"""

    pass


a = 0
b = 0

try:
    a = int(input("Digita un número: "))
    b = int(input("Digita otro número: "))
    if b == 2:
        raise DivisionError("No está permitido el calculo por 2")
    resultado = a / b
    print(f"Resultado: {resultado}")
except ValueError:
    print("El valor que digitó no es un número válido")
except ZeroDivisionError:
    print("No está permitido dividir por 0")
finally:
    print("Print desde finally")

print("Este es otro print")