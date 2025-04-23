import random 

countries = {'col', 'mex', 'bol', 'pe'}
result_population_mayor = {}

population_v2 = {country : random.randint(1, 100) for country in countries }
print(population_v2)

result_population_mayor = { country : population for (country, population) in population_v2.items() if population > 50 }

print(result_population_mayor)



