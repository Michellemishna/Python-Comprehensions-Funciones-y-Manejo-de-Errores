dict = {}
#diccionario con comprehension
for i in range(1, 11):
  dict[i] = i * 2
print(dict)

#diccionario con comprehension dentro del diccionarxio esto simplifica el codigo a una sola linea
dict_v2 = {i: i * 2 for i in range(1, 11)}

import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
  population[country] = random.randint(1, 100)

print(population)

#crea un diccionario con los paises como claves y la poblacion como valores
#diccionario con comprehension de la forma mas sencilla
population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

#zip se usa para unir dos listas en una lista de tuplas
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]
print(list(zip(names, ages)))
#crea un dictionario con las tuplas de las listas
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)