import random 

countries = {'col', 'mex', 'bol', 'pe'}
population = {}


for i in countries:
    population[i] = random.randint(1, 100)

print(population) ## col:100, mex:1, bol:2, pe:140

## ahora

population_v2 = {country : random.randint(1, 100) for country in countries}
print(population_v2)