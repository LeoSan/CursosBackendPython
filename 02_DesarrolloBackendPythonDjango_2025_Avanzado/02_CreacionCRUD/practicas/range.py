# generando un rango con valores de 0 al número indicado
	for i in range(10):	# genera una secuencia 0 - 9
		pass

# estableciendo los valores de la secuencia en range()
	range(start, stop, step_size)

print(range(10))
	# range(0, 10)

print(list(range(10)))
	# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(2, 8)))
	# [2, 3, 4, 5, 6, 7]

print(list(range(2, 20, 3)))
	# [2, 5, 8, 11, 14, 17]



genre = ['pop', 'rock', 'jazz']

for i in range(len(genre)):
    print(i)
	# 0
	# 1
	# 2



genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in genre:
    print('I like', i)

# Resultado: 
#I like pop
#I like rock
#I like jazz