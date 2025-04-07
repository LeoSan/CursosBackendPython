import json, pandas, numpy

## Comando para generar entornos -> python3 -m venv nom_entorno
## Comando para activar entorno -> source mi_entorno/bin/activate
## para importar a tu entorno pip podemos acceder al shell de python con este comando ´python´ ó ´python3´ 
## Luego que entramos al shell podemos import pip 
## luego nos salimos exit
## luego validamos si esta instaldo which pip esto nos indicará si esta instaldo en nuestro entorno o de manera global, nos indicará la ruta donde esta implementado si no muestra nada o sale error toca instalarlo 
## este comando para instalarlo en tu entorno activado -> python -m pip install pandas
## Por ultimo y para validar ya deberia salir en el listado pip list para est caso logre instalarlo para la version 3.13 de python


archivo_json = "/Users/leonard/CursosBackendPython/Primeros_pasos_Python/CursoPython/Practicas/Basicas/Products.json"
new_product = {
    "name": "Prueba",
    "price": 100,
    "quantity": 100,
    "brand": "Marca Patito",
    "category": "Accessories",
    "entry_date": "2025-04-07"
}


#Lectura 
with open(archivo_json, 'r') as file:
    products = json.load(file)
    for product in products:
        print(f"Product: {product['name']}, Categoria:  {product['category']}, Precio:  {product['price']}    ")


#escritura 
products.append(new_product)

with open(archivo_json, mode='w') as file:
    json.dump(products, file, indent=4)
    for product in products:
        print(f"Product: {product['name']}, Categoria:  {product['category']}, Precio:  {product['price']}    ")
