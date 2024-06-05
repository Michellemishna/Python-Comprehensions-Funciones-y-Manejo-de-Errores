import random
countries = ['col', 'mex', 'bol', 'pe']

# #crea un diccionario con los paises como claves y la poblacion como valores
population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

# #crea un diccionario con los paises como claves y la poblacion como valores pero con condicion
result = {country: population for (country, population) in population_v2.items() if population > 50}
print(result)

# #crea un diccionario con las vocales de una cadena
text = 'Hola, soy Nicolas'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)


#list es mutable, ordenada, indexing/slicing, acepta elementos duplicados 
#tupla no es mutable, es ordenada, indexing/slicing, acepta elementos duplicados 
#set es mutable, no ordenada, no indexing/slicing, no acepta elementos duplicados