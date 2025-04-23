## ejemplo usando Lista con dicionarios adentro 

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

##print(matches)
##print(len(matches))

new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))

def condicionalJuego(item):#Recurda dentro de filter o map recibe el iterable, envias la lista completa en su parametro pero la funmcion lambda o funcion que construllas recibe el iterable
    if item['home_team_result'] == 'Win':
        return item

new_list_func = list(filter(condicionalJuego, matches))

##print(new_list)
print(len(new_list))

##print(matches)
print(len(matches))

##print(new_list_func)
print(len(new_list_func))


