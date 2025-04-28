import requests 

def get_categorias():
    r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10&offset=0')
    resultado = r.json() 
    categorias = resultado["results"]
    #print(categorias)
    for categoria in categorias:
        print(categoria['name'])
