
lista_jugadores = [
    [
        {
            "nombre": "Leo001",
            "fecha": "2025-04-24T00:17:01.380015",
            "tiempo": 22.876988,
            "categoria": "cocina",
            "palabra_secreta": "estufa",
            "nivel": "medio",
            "win": 1
        }
    ],
    [
        {
            "nombre": "Leo002",
            "fecha": "2025-04-24T00:17:36.669573",
            "tiempo": 23.686107,
            "categoria": "humano",
            "palabra_secreta": "estomago",
            "nivel": "medio",
            "win": 1
        }
    ],
    [
        {
            "nombre": "Leo004",
            "fecha": "2025-04-24T00:22:52.785446",
            "tiempo": 19.148849,
            "categoria": "cocina",
            "palabra_secreta": "pala",
            "nivel": "medio",
            "win": 0
        }
    ],
    [
        {
            "nombre": "leo005",
            "fecha": "2025-04-24T00:24:04.538114",
            "tiempo": 17.51441,
            "categoria": "cocina",
            "palabra_secreta": "pala",
            "nivel": "medio",
            "win": 0
        }
    ],
    [
        {
            "nombre": "Jose",
            "fecha": "2025-04-28T14:11:59.083892",
            "tiempo": 27.526995,
            "categoria": "pais",
            "palabra_secreta": "colombia",
            "nivel": "medio",
            "win": 0
        }
    ],
    [
        {
            "nombre": "daniel",
            "fecha": "2025-04-28T14:24:41.658011",
            "tiempo": 25.046599,
            "categoria": "cocina",
            "palabra_secreta": "nevera",
            "nivel": "medio",
            "win": 1
        }
    ]
]

"""
resultado = [['win','loser'], [0, 0]]
for filas in lista_jugadores:
    if filas[0]['win'] == 1:
        resultado[1][0] +=1
    else:
        resultado[1][1] +=1

print(resultado[0])
print(resultado[1])
""" 

wins = sum(jugador[0]['win'] == 1 for jugador in lista_jugadores)
losers = len(lista_jugadores) - wins

resultado = [['win', 'loser'], [wins, losers]]

print(resultado[0])
print(resultado[1])

