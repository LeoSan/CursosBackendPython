numeros = [1, 2, 3, 4, 5]

def cuadrado(n):
  return n ** 2

resultados = map(cuadrado, numeros)
print(resultados)  # Output: <map object at 0x...>
print(list(resultados))  # Output: [1, 4, 9, 16, 25]

## Otro ejemplo 
numeros_str = ["10", "20", "30"]
numeros_int = map(int, numeros_str)
print(list(numeros_int))  # Output: [10, 20, 30]


numeros = [1, 2, 3]
dobles = map(lambda x: x * 2, numeros)
print(list(dobles))  # Output: [2, 4, 6]


items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

def add_taxes(item):
  new_item = item.copy()
  new_item['taxes'] = new_item['price'] * .19
  return new_item

new_items = list(map(add_taxes, items))
print('New list')
print(new_items)
print('Old list')
print(items)