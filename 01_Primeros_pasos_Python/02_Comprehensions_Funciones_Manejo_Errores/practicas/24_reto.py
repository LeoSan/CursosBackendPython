
def filter_by_length(word):
    # Escribe tu solución 👇
    if len(word) >= 4:
        return word
    
def filter_by_length_con_lambda(words):
   # Escribe tu solución 👇
   return list(filter(lambda numLetters: len(numLetters) >= 4, words))

words1 = ['amor', 'sol', 'piedra', 'día']
words2 = ['rosa', 'gol', 'pez', 'día', 'gafas']
words3 = ['aa', 'a', 'bb', 'cc']
response = list(filter(filter_by_length, words1))
print(response)