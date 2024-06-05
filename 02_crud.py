set_countries = {'col', 'mex', 'bol'}

# para saber el tamaño del conjunto usamos len()
size = len(set_countries)
print(size)

# para saber si un elemento esta dentro del conjunto usamos in
print('col' in set_countries)
print('pe' in set_countries)

# para agregar un elemento al conjunto usamos add()
set_countries.add('pe')
print(set_countries)

# para actualizar un conjunto usamos update()
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# para eliminar un elemento del conjunto usamos remove()
set_countries.remove('col')
print(set_countries)

# para eliminar un elemento del conjunto usamos discard() al no encontrar el elemento no genera error
set_countries.discard('arg')
print(set_countries)

# para eliminar todos los elementos del conjunto usamos clear()
set_countries.clear()
print(set_countries)



