def multiply_numbers(n):
    # Escribe tu solución 👇
    return n*2

numbers = [1, 2, 3, 4]
response = map( multiply_numbers, numbers)

print(numbers)
print(list(response))

## Ejemplo dos 


def multiply_numbers(numbers):
    # Escribe tu solución 👇
    result = list(map(lambda number: number * 2, numbers))
    return result

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)